from modules.student_manager import get_student_by_id
from modules.dataset_manager import get_all_datasets
from modules.analytics import evaluate_student_record
from modules.config_loader import load_config
from modules.analytics import classify_performance

def get_student_record_from_dataset(dataset, student_id):
    for record in dataset.get("records", []):
        if str(record["student_id"]) == str(student_id):
            return record
    return None


def get_student_history_datasets(student_id):
    datasets = get_all_datasets()
    result_list = []

    if not datasets:
        return []

    for dataset in datasets:
        record = get_student_record_from_dataset(dataset, student_id)
        if record is not None:
            result_list.append(dataset)

    return result_list


def build_student_history_entry(dataset, student_record):
    return {
        "exam_name": dataset["exam_name"],
        "exam_date": dataset["exam_date"],
        "dataset_type": dataset["type"],
        "institution": dataset["institution"],
        "board": dataset["board"],
        "batch": dataset["batch"],
        "student_id": student_record["student_id"],
        "marks": student_record["marks"]
    }


def get_student_academic_history(student_id):
    student = get_student_by_id(student_id)
    if not student:
        return {
            "status": "error",
            "message":"Student not found."
        }

    matching_datasets = get_student_history_datasets(student_id)
    if not matching_datasets:
        return {
            "status": "error",
            "message":"No academic history has been found for this student."
        }

    history = []

    for dataset in matching_datasets:
        exam_date = dataset.get("exam_date")
        if not exam_date:
            return {
                "status":"error",
                "message":"One or more datasets are missing exam date."
            }

        student_record = get_student_record_from_dataset(dataset, student_id)
        if student_record is not None:
            history_entry = build_student_history_entry(dataset, student_record)
            history.append(history_entry)

    history.sort(key=lambda entry: entry["exam_date"])

    return {
        "status":"success",
        "history": history
    }


    

    

def build_performance_series_entry(history_entry,config):
   record = {
    "student_id": history_entry["student_id"],
    "marks": history_entry["marks"]
    }
   evaluated_student=evaluate_student_record(record,config)
   performance_series={
    
    "exam_name": history_entry["exam_name"],
    "exam_date": history_entry["exam_date"],
    "dataset_type": history_entry["dataset_type"],
    "institution": history_entry["institution"],
    "board": history_entry["board"],
    "batch": history_entry["batch"],

    
    "student_id": evaluated_student["student_id"],
    "marks": evaluated_student["marks"],
    "total": evaluated_student["total"],
    "average": evaluated_student["average"],
    "gpa": evaluated_student["gpa"],
    "strongest_subject": evaluated_student["strongest_subject"],
    "weakest_subject": evaluated_student["weakest_subject"],
    "weak_subjects": evaluated_student["weak_subjects"],
    "weak_subject_count": evaluated_student["weak_subject_count"],
    "performance": evaluated_student["performance"]
  }
   return performance_series



def build_student_performance_series(student_id):
    history_result = get_student_academic_history(student_id)
    if history_result["status"] == "error":
        return history_result
    history = history_result["history"]
    config = load_config()
    student_performance_series=[]
    for entry in history:
        student_performance_series.append(build_performance_series_entry(entry,config))
    return {
       "status": "success",
       "performance_series": student_performance_series
         }


def calculate_metric_change(previous_value,current_value):
    return current_value-previous_value

def classify_metric_trend(change,improvement_margin,decline_margin):
    if change>=improvement_margin:
        return "improving"
    elif change<=decline_margin:
        return "declining"
    else:
        return "stable"

def build_trend_steps(performance_series):
    if not performance_series:
        return []
    if len(performance_series)<2:
        return []
    comparisons=[]
    i=0
    while i<(len(performance_series)-1):
        previous_series=performance_series[i]
        next_series=performance_series[i+1]
        avg_change=calculate_metric_change(previous_series["average"],next_series["average"])
        gpa_change=calculate_metric_change(previous_series["gpa"],next_series["gpa"])
        weak_subject_count_change=calculate_metric_change(previous_series["weak_subject_count"],next_series["weak_subject_count"])


        exam_change={ "from_exam":previous_series["exam_name"],
                     "to_exam":next_series["exam_name"],
                     "from_date":previous_series["exam_date"],
                     "to_date":next_series["exam_date"],
                     "average_change":avg_change,
                     "gpa_change":gpa_change,
                     "weak_subject_count_change":weak_subject_count_change

                       }
        comparisons.append(exam_change)
        i=i+1
    return comparisons


def extract_metric_changes(trend_steps, metric_name):
    if not trend_steps:
        return []

    valid_metrics = ["average_change", "gpa_change", "weak_subject_count_change"]
    if metric_name not in valid_metrics:
        return []

    extracted_changes = []
    for step in trend_steps:
        extracted_changes.append(step[metric_name])

    return extracted_changes


def summarize_metric_trend(change_list, trend_config, metric_name):
    if not change_list:
        return {
            "trend": "stable",
            "improvement_count": 0,
            "decline_count": 0,
            "stable_count": 0
        }

    improvement_margin = trend_config["improvement_margin"]
    decline_margin = trend_config["decline_margin"]

    improvement_count = 0
    decline_count = 0
    stable_count = 0

    for change in change_list:
        if metric_name in ["average", "gpa"]:
            if change >= improvement_margin:
                improvement_count += 1
            elif change <= decline_margin:
                decline_count += 1
            else:
                stable_count += 1

        elif metric_name == "weak_subject_count":
            if change <= improvement_margin:
                improvement_count += 1
            elif change >= decline_margin:
                decline_count += 1
            else:
                stable_count += 1

    if improvement_count > decline_count and improvement_count >= stable_count:
        final_trend = "improving"
    elif decline_count > improvement_count and decline_count >= stable_count:
        final_trend = "declining"
    elif stable_count > improvement_count and stable_count > decline_count:
        final_trend = "stable"
    else:
        final_trend = "mixed"

    return {
        "trend": final_trend,
        "improvement_count": improvement_count,
        "decline_count": decline_count,
        "stable_count": stable_count
    }


def determine_overall_trend(average_trend,gpa_trend,weak_subject_trend):
    if not average_trend:
        return "mixed"
    if not gpa_trend:
        return "mixed"
    if not weak_subject_trend:
        return "mixed" 
    trend_labels=[average_trend["trend"],gpa_trend["trend"],weak_subject_trend["trend"]]
    if trend_labels[0]==trend_labels[1]==trend_labels[2]:
        return trend_labels[0]
    elif trend_labels.count("improving")==2:
        return "improving"
    elif trend_labels.count("declining")==2:
        return "declining"
    elif trend_labels.count("stable")==2:
        return "stable"
    elif trend_labels.count("mixed")==2:
        return "mixed"
    
    else:
        return "mixed"
    

def analyze_student_trend(student_id):
    result=build_student_performance_series(student_id)
    if result["status"] == "error":
           return result
    performance_series = result["performance_series"]
    if len(performance_series)<2:
        return {
    "status": "error",
    "message": "At least 2 exam records are required for trend analysis."
           }
    config = load_config()
    trend_config = config["trend_thresholds"]
    trend_steps = build_trend_steps(performance_series)
    average_changes = extract_metric_changes(trend_steps, "average_change")
    gpa_changes = extract_metric_changes(trend_steps, "gpa_change")
    weak_subject_changes = extract_metric_changes(trend_steps, "weak_subject_count_change") 
    average_trend = summarize_metric_trend(
    average_changes,
    trend_config["average"],
    "average"
              )    
    gpa_trend = summarize_metric_trend(
    gpa_changes,
    trend_config["gpa"],
    "gpa"
      )     
    weak_subject_trend = summarize_metric_trend(
    weak_subject_changes,
    trend_config["weak_subject_count"],
    "weak_subject_count"
            )  
    overall_trend = determine_overall_trend(
    average_trend,
    gpa_trend,
    weak_subject_trend
         )
    return {
    "status": "success",
    "student_id": student_id,
    "trend_steps": trend_steps,
    "average_trend": average_trend,
    "gpa_trend": gpa_trend,
    "weak_subject_trend": weak_subject_trend,
    "overall_trend": overall_trend
        }




def get_latest_performance_entry(performance_series):
    if not performance_series:
        return None
    return performance_series[-1]


def count_declining_steps(change_list, trend_config, metric_name):
    if not change_list:
        return 0
    if metric_name not in ["average", "gpa", "weak_subject_count"]:
        return 0
    if metric_name=="average":
        decline_margin = trend_config["decline_margin"]        
        decline_count=0
        for change in change_list:
            if change<=decline_margin:
                decline_count+=1
        return decline_count
    elif metric_name=="gpa":
        decline_margin = trend_config["decline_margin"]  
        decline_count=0
        for change in change_list:
            if change<=decline_margin:
                decline_count+=1
        return decline_count
    elif metric_name=="weak_subject_count":
        decline_margin = trend_config["decline_margin"]  
        decline_count=0
        for change in change_list:
            if change>=decline_margin:
                decline_count+=1
        return decline_count
    
    
    
    
    
def build_risk_flags(latest_entry, trend_result, config):
    risk_flags = {
        "low_gpa": False,
        "high_weak_subject_burden": False,
        "declining_average_trend": False,
        "declining_gpa_trend": False,
        "worsening_weak_subject_trend": False,
        "overall_declining_trend": False,
        "repeated_decline": False
    }

    low_gpa = False
    high_weak_subject_burden = False
    declining_average_trend = False
    declining_gpa_trend = False
    worsening_weak_subject_trend = False
    overall_declining_trend = False
    repeated_decline = False

    if not latest_entry:
        return risk_flags

    min_gpa = config["risk_rules"]["min_gpa"]
    if latest_entry["gpa"] < min_gpa:
        low_gpa = True

    max_weak_subjects = config["risk_rules"]["max_weak_subjects"]
    if latest_entry["weak_subject_count"] >= max_weak_subjects:
        high_weak_subject_burden = True

    if not trend_result or trend_result["status"] == "error":
        risk_flags = {
            "low_gpa": low_gpa,
            "high_weak_subject_burden": high_weak_subject_burden,
            "declining_average_trend": declining_average_trend,
            "declining_gpa_trend": declining_gpa_trend,
            "worsening_weak_subject_trend": worsening_weak_subject_trend,
            "overall_declining_trend": overall_declining_trend,
            "repeated_decline": repeated_decline
        }
        return risk_flags

    if trend_result["average_trend"]["trend"] == "declining":
        declining_average_trend = True

    if trend_result["gpa_trend"]["trend"] == "declining":
        declining_gpa_trend = True

    if trend_result["weak_subject_trend"]["trend"] == "declining":
        worsening_weak_subject_trend = True

    if trend_result["overall_trend"] == "declining":
        overall_declining_trend = True

    trend_steps = trend_result["trend_steps"]

    average_changes = extract_metric_changes(trend_steps, "average_change")
    gpa_changes = extract_metric_changes(trend_steps, "gpa_change")
    weak_subject_changes = extract_metric_changes(trend_steps, "weak_subject_count_change")

    average_decline_count = count_declining_steps(
        average_changes,
        config["trend_thresholds"]["average"],
        "average"
    )

    gpa_decline_count = count_declining_steps(
        gpa_changes,
        config["trend_thresholds"]["gpa"],
        "gpa"
    )

    weak_subject_decline_count = count_declining_steps(
        weak_subject_changes,
        config["trend_thresholds"]["weak_subject_count"],
        "weak_subject_count"
    )

    required_decline_count = config["risk_rules"]["decline_count"]

    if average_decline_count >= required_decline_count:
        repeated_decline = True
    if gpa_decline_count >= required_decline_count:
        repeated_decline = True
    if weak_subject_decline_count >= required_decline_count:
        repeated_decline = True

    risk_flags = {
        "low_gpa": low_gpa,
        "high_weak_subject_burden": high_weak_subject_burden,
        "declining_average_trend": declining_average_trend,
        "declining_gpa_trend": declining_gpa_trend,
        "worsening_weak_subject_trend": worsening_weak_subject_trend,
        "overall_declining_trend": overall_declining_trend,
        "repeated_decline": repeated_decline
    }

    return risk_flags



def build_risk_reasons(risk_flags):
    if not risk_flags:
        return []
    reasons=[]
    if risk_flags["low_gpa"]:
        reasons.append("Latest GPA is below the minimum acceptable threshold.")
    if risk_flags["high_weak_subject_burden"]:
        reasons.append("Current weak subject burden is above the allowed limit.")
    
    if risk_flags["declining_average_trend"]:
        reasons.append("Average trend is declining across exams.")
    if risk_flags["declining_gpa_trend"]:
        reasons.append("GPA trend is declining across exams.")
    if risk_flags["worsening_weak_subject_trend"]:
        reasons.append("Weak subject burden is worsening over time.")
    if risk_flags["overall_declining_trend"]:
        reasons.append("Overall Academic Trend is declining.")
    if risk_flags["repeated_decline"]:
        reasons.append("Repeated decline has been detected across performance history.")
    return reasons 


def calculate_risk_score(risk_flags,config):
    if not risk_flags:
        return 0
    risk_score=0
    for flag_name, flag_value in risk_flags.items():
     if flag_value:
        risk_score=risk_score+ config["risk_scoring"][flag_name]
    return risk_score 



def classify_risk_level(risk_score,config):
    risk_levels=config["risk_levels"]
    for level,level_range in risk_levels.items():
        if level_range["min_score"]<=risk_score<=level_range["max_score"]:
            return level
        
    return "low" 
        

def analyze_student_risk(student_id):
    performance_result=build_student_performance_series(student_id)
    if performance_result["status"]=="error":
        return performance_result
    performance_series = performance_result["performance_series"]
    latest_entry=get_latest_performance_entry(performance_series)
    if not latest_entry:
        return {
    "status": "error",
    "message": "No performance records found for risk analysis."
           }
    config=load_config()
    
    trend_analysis=analyze_student_trend(student_id)
    risk_flags=build_risk_flags(latest_entry, trend_analysis, config)
    risk_reasons=build_risk_reasons(risk_flags)
    risk_score=calculate_risk_score(risk_flags,config)
    risk_level=classify_risk_level(risk_score,config)
    at_risk = risk_level in config["risk_policies"]["at_risk_levels"]
    
    current_snapshot={
    "average": latest_entry["average"],
    "gpa": latest_entry["gpa"],
    "weak_subject_count": latest_entry["weak_subject_count"],
    "performance": latest_entry["performance"]
        }  
    if not trend_analysis["status"]=="error":
     trend_snapshot={
     "average_trend": trend_analysis["average_trend"]["trend"],
     "gpa_trend": trend_analysis["gpa_trend"]["trend"],
     "weak_subject_trend": trend_analysis["weak_subject_trend"]["trend"],
     "overall_trend": trend_analysis["overall_trend"]
             }  
    if trend_analysis["status"]=="error":
         trend_snapshot={
            "average_trend": None,
            "gpa_trend": None,
            "weak_subject_trend": None,
            "overall_trend": None
           }
    
    final_analysis={
    "status": "success",
    "student_id": student_id,
    "latest_exam": latest_entry["exam_name"],
    "latest_exam_date": latest_entry["exam_date"],
    "current_snapshot": current_snapshot,
        
    "trend_snapshot": trend_snapshot,
    
    "risk_flags":risk_flags,
    "risk_reasons": risk_reasons,
    "risk_score": risk_score,
    "risk_level": risk_level,
    "at_risk": at_risk
        }
    

    return final_analysis 



def calculate_mean(values):
    if not values:
        return 0
    return (sum(values)/len(values))


def extract_series_metric_values(performance_series,metric_name):
    if not performance_series:
        return []
    valid_metrics=["gpa","average","weak_subject_count"]
    if metric_name not in valid_metrics:
        return []
    extracted_changes = []
    for values in performance_series:
        extracted_changes.append(values[metric_name])

    return extracted_changes


def calculate_prediction_value(recent_value, historical_mean, trend_mean_change, weights):
   return ((recent_value*weights["recent"])+
           (historical_mean*weights["average"])+
           ((recent_value+trend_mean_change)*weights["trend"])
          )


def finalize_prediction_outputs(predicted_average, predicted_gpa, predicted_weak_subject_count):
    rounded_average=round(predicted_average,2)
    rounded_gpa=round(predicted_gpa,2)
    rounded_weak_subject_count=round(predicted_weak_subject_count)
    if rounded_weak_subject_count<0:
        rounded_weak_subject_count=0
    return {"average":rounded_average,
            "gpa":rounded_gpa,
            "weak_subject_count":rounded_weak_subject_count}



def predict_student_performance(student_id):
    performance_series = build_student_performance_series(student_id)

    if performance_series["status"] == "error":
      return performance_series

    student_performance_series = performance_series["performance_series"]
    config=load_config()
    if len(student_performance_series)<config["prediction_rules"]["min_datasets_required"]:
        return {
    "status": "error",
    "message": "At least 2 exam records are required for prediction."
        }
    
    latest_entry = get_latest_performance_entry(student_performance_series)
    trend_result = analyze_student_trend(student_id)
    if trend_result["status"]=="error":
        return trend_result
    average_values=extract_series_metric_values(student_performance_series,"average")
    average_historical_mean=calculate_mean(average_values)
    gpa_values=extract_series_metric_values(student_performance_series,"gpa")
    gpa_historical_mean=calculate_mean(gpa_values)
    weak_subject_count_values=extract_series_metric_values(student_performance_series,"weak_subject_count")
    weak_subject_count_historical_mean=calculate_mean(weak_subject_count_values)
    trend_steps=trend_result["trend_steps"]
    avg_change_list=extract_metric_changes(trend_steps,"average_change")
    gpa_change_list=extract_metric_changes(trend_steps,"gpa_change")
    weak_subject_count_change_list=extract_metric_changes(trend_steps,"weak_subject_count_change")
    avg_trend_mean=calculate_mean(avg_change_list)
    gpa_trend_mean=calculate_mean(gpa_change_list)
    weak_subject_trend_mean=calculate_mean(weak_subject_count_change_list) 
    recent_average=latest_entry["average"]
    recent_gpa=latest_entry["gpa"]
    recent_weak_subject_count=latest_entry["weak_subject_count"]
    
    weights=config["prediction_weights"]
    predicted_average=calculate_prediction_value(recent_average,average_historical_mean,avg_trend_mean,weights)
    predicted_gpa=calculate_prediction_value(recent_gpa,gpa_historical_mean,gpa_trend_mean,weights)
    predicted_weak_subject_count=calculate_prediction_value(recent_weak_subject_count,weak_subject_count_historical_mean,weak_subject_trend_mean,weights)
    finalized_prediction=finalize_prediction_outputs(predicted_average,predicted_gpa,predicted_weak_subject_count)
    predicted_performance=classify_performance(finalized_prediction["average"],config["performance_levels"])
    prediction_basis={
    "recent_exam": latest_entry["exam_name"],
    "recent_exam_date": latest_entry["exam_date"],
    "history_count": len(student_performance_series)
      }
    prediction_components={
    "average": {
        "recent_value": latest_entry["average"],
        "historical_mean": average_historical_mean,
        "trend_mean_change": avg_trend_mean
    },
    "gpa": {
        "recent_value": latest_entry["gpa"],
        "historical_mean": gpa_historical_mean,
        "trend_mean_change": gpa_trend_mean
    },
    "weak_subject_count": {
        "recent_value": latest_entry["weak_subject_count"],
        "historical_mean": weak_subject_count_historical_mean,
        "trend_mean_change": weak_subject_trend_mean
    }
       }

    finalized_prediction_output={
        "status": "success",
        "student_id":student_id,
        "prediction_basis":prediction_basis,
        "predicted_metrics":finalized_prediction,
        "predicted_performance":predicted_performance,
        "prediction_components":prediction_components,
    }

    return finalized_prediction_output


def compare_internal_board_performance(
    student_id,
    internal_exam_name,
    board_exam_name):
    result = build_student_performance_series(student_id)

    if result["status"] == "error":
         return result

    performance_series = result["performance_series"]

    internal_exam = None
    board_exam = None

    for entry in performance_series:

        if entry["exam_name"] == internal_exam_name:
            internal_exam = entry
        if entry["exam_name"] == board_exam_name:
            board_exam = entry

    if not internal_exam:
        return {
            "status": "error",
            "message": "Internal examination was not found for this student."}

    if not board_exam:
        return {
            "status": "error",
            "message": "Board examination was not found for this student."}

    if internal_exam["dataset_type"] != "internal":
        return {
            "status": "error",
            "message": "Selected internal examination is not an internal dataset."}

    if board_exam["dataset_type"] != "board":
        return {
            "status": "error",
            "message": "Selected board examination is not a board dataset."}

    internal_average = internal_exam["average"]
    board_average = board_exam["average"]

    average_gap = round(board_average - internal_average,2)

    if internal_average == 0:
        retention_percentage = None
    else:
        retention_percentage = round(
            (board_average / internal_average) * 100, 2)

    subject_gaps = {}

    for subject in internal_exam["marks"]:

        if subject in board_exam["marks"]:

            internal_mark = internal_exam["marks"][subject]
            board_mark = board_exam["marks"][subject]

            subject_gaps[subject] = {
             "internal": internal_mark,
              "board": board_mark,
              "gap": board_mark - internal_mark
               }
 
    largest_decline_subject = None
    largest_decline = None

    if subject_gaps:

     largest_decline_subject = min(
        subject_gaps,
        key=lambda subject: subject_gaps[subject]["gap"]
        )

     largest_decline = subject_gaps[largest_decline_subject]["gap"]


    
    return {
        "status": "success",
        "student_id": student_id,

        "internal_exam": internal_exam["exam_name"],
        "board_exam": board_exam["exam_name"],

        "internal_average": internal_average,
        "board_average": board_average,

        "average_gap": average_gap,
        "retention_percentage": retention_percentage,

        "subject_gaps": subject_gaps,

        "largest_decline_subject": largest_decline_subject,
        "largest_decline": largest_decline
    }



def analyze_weakness_persistence(student_id):

    result = build_student_performance_series(student_id)

    if result["status"] == "error":
        return result

    performance_series = result["performance_series"]

    if not performance_series:
        return {
            "status": "error",
            "message": "No performance history found for this student."
        }

    config = load_config()
    weak_subject_mark = config["risk_rules"]["weak_subject_mark"]

    subjects = performance_series[0]["marks"].keys()

    subject_results = {}

    for subject in subjects:

        total_exams = 0
        weak_exams = 0
        current_mark = None

        for entry in performance_series:

            if subject not in entry["marks"]:
                continue

            mark = entry["marks"][subject]

            total_exams += 1

            if mark < weak_subject_mark:
                weak_exams += 1

            current_mark = mark

        if total_exams == 0:
            continue

        persistence_percentage = round(
            (weak_exams / total_exams) * 100,
            2
        )

        subject_results[subject] = {
            "total_exams": total_exams,
            "weak_exams": weak_exams,
            "persistence_percentage": persistence_percentage,
            "current_mark": current_mark,
            "currently_weak": current_mark < weak_subject_mark
        }

    persistent_weaknesses = []

    for subject, result in subject_results.items():

        if result["weak_exams"] >= 2:
            persistent_weaknesses.append(subject)

    return {
        "status": "success",
        "student_id": student_id,
        "subjects": subject_results,
        "persistent_weaknesses": persistent_weaknesses
    } 


def calculate_standard_deviation(values):
    if not values:
        return 0

    mean = sum(values) / len(values)

    squared_differences = []

    for value in values:
        difference = value - mean
        squared_differences.append(difference ** 2)

    variance = sum(squared_differences) / len(values)

    return variance ** 0.5


def analyze_academic_stability(student_id):

    performance_result = build_student_performance_series(student_id)

    if performance_result["status"] == "error":
        return performance_result

    performance_series = performance_result["performance_series"]

    if len(performance_series) < 2:
        return {
            "status": "error",
            "message": "At least 2 exam records are required for stability analysis."
        }

    trend_result = analyze_student_trend(student_id)

    if trend_result["status"] == "error":
        return trend_result

    average_values = []

    for entry in performance_series:
        average_values.append(entry["average"])

    performance_mean = round(
        sum(average_values) / len(average_values),
        2
    )

    performance_standard_deviation = round(
        calculate_standard_deviation(average_values),
        2
    )

    average_changes = extract_metric_changes(
        trend_result["trend_steps"],
        "average_change"
    )

    absolute_changes = []

    for change in average_changes:
        absolute_changes.append(abs(change))

    if absolute_changes:
        average_absolute_change = round(
            sum(absolute_changes) / len(absolute_changes),
            2
        )

        largest_average_change = max(absolute_changes)
    else:
        average_absolute_change = 0
        largest_average_change = 0

    largest_average_change = round(
        largest_average_change,
        2
    )

    trend_labels = []

    for step in trend_result["trend_steps"]:

        average_change = step["average_change"]

        if average_change >= 5:
            trend_labels.append("improving")

        elif average_change <= -5:
            trend_labels.append("declining")

        else:
            trend_labels.append("stable")

    improvement_steps = trend_labels.count("improving")
    decline_steps = trend_labels.count("declining")
    stable_steps = trend_labels.count("stable")

    direction_changes = 0

    previous_direction = None

    for label in trend_labels:

        if label == "stable":
            continue

        if previous_direction is not None:
            if label != previous_direction:
                direction_changes += 1

        previous_direction = label

    if improvement_steps == len(trend_labels):
        stability_status = "consistently improving"

    elif decline_steps == len(trend_labels):
        stability_status = "consistently declining"

    elif direction_changes >= 1:
        stability_status = "volatile"

    else:
        stability_status = "stable"

    return {
        "status": "success",
        "student_id": student_id,
        "exam_count": len(performance_series),

        "average_performance": performance_mean,
        "performance_standard_deviation":
            performance_standard_deviation,

        "average_absolute_change": average_absolute_change,
        "largest_average_change": largest_average_change,

        "improvement_steps": improvement_steps,
        "decline_steps": decline_steps,
        "stable_steps": stable_steps,

        "direction_changes": direction_changes,

        "stability_status": stability_status
    } 


def analyze_improvement_momentum(student_id):

    performance_result = build_student_performance_series(student_id)

    if performance_result["status"] == "error":
        return performance_result

    performance_series = performance_result["performance_series"]

    if len(performance_series) < 3:
        return {
            "status": "error",
            "message": "At least 3 exam records are required for momentum analysis."
        }

    trend_result = analyze_student_trend(student_id)

    if trend_result["status"] == "error":
        return trend_result

    trend_steps = trend_result["trend_steps"]

    average_changes = extract_metric_changes(
        trend_steps,
        "average_change"
    )

    if len(average_changes) < 2:
        return {
            "status": "error",
            "message": "At least 3 exam records are required for momentum analysis."
        }

    recent_change = average_changes[-1]

    earlier_changes = average_changes[:-1]

    earlier_average_change = (
        sum(earlier_changes) / len(earlier_changes)
    )

    momentum = recent_change - earlier_average_change

    momentum = round(momentum, 2)
    earlier_average_change = round(earlier_average_change, 2)
    recent_change = round(recent_change, 2)

    if momentum > 0:
        momentum_direction = "strengthening"

    elif momentum < 0:
        momentum_direction = "weakening"

    else:
        momentum_direction = "stable"

    return {
        "status": "success",
        "student_id": student_id,
        "exam_count": len(performance_series),
        "recent_change": recent_change,
        "earlier_average_change": earlier_average_change,
        "momentum": momentum,
        "momentum_direction": momentum_direction
    } 


    

def analyze_subject_comovement(student_id):

    performance_result = build_student_performance_series(student_id)

    if performance_result["status"] == "error":
        return performance_result

    performance_series = performance_result["performance_series"]

    if len(performance_series) < 4:
        return {
            "status": "error",
            "message": "At least 4 exam records are required for subject co-movement analysis."
        }

    subjects = list(performance_series[0]["marks"].keys())

    subject_pairs = []

    for i in range(len(subjects)):

        for j in range(i + 1, len(subjects)):

            first_subject = subjects[i]
            second_subject = subjects[j]

            same_direction_count = 0
            opposite_direction_count = 0
            comparable_count = 0

            for exam_index in range(len(performance_series) - 1):

                current_exam = performance_series[exam_index]
                next_exam = performance_series[exam_index + 1]

                if first_subject not in current_exam["marks"]:
                    continue

                if first_subject not in next_exam["marks"]:
                    continue

                if second_subject not in current_exam["marks"]:
                    continue

                if second_subject not in next_exam["marks"]:
                    continue

                first_change = (
                    next_exam["marks"][first_subject]
                    - current_exam["marks"][first_subject]
                )

                second_change = (
                    next_exam["marks"][second_subject]
                    - current_exam["marks"][second_subject]
                )

                if first_change == 0 or second_change == 0:
                    continue

                comparable_count += 1

                if (
                    (first_change > 0 and second_change > 0)
                    or
                    (first_change < 0 and second_change < 0)
                ):
                    same_direction_count += 1

                else:
                    opposite_direction_count += 1

            if comparable_count == 0:
                co_movement_percentage = None

            else:
                co_movement_percentage = round(
                    (same_direction_count / comparable_count) * 100,
                    2
                )

            subject_pairs.append({
                "subject_1": first_subject,
                "subject_2": second_subject,
                "same_direction_count": same_direction_count,
                "opposite_direction_count": opposite_direction_count,
                "comparable_count": comparable_count,
                "co_movement_percentage": co_movement_percentage
            })

    return {
        "status": "success",
        "student_id": student_id,
        "exam_count": len(performance_series),
        "subject_pairs": subject_pairs
    } 
    

def analyze_exam_context(student_id, exam_name):

    datasets = get_all_datasets()

    selected_dataset = None

    for dataset in datasets:
        if dataset["exam_name"] == exam_name:
            selected_dataset = dataset
            break

    if not selected_dataset:
        return {
            "status": "error",
            "message": "Exam dataset was not found."
        }

    student_record = get_student_record_from_dataset(
        selected_dataset,
        student_id
    )

    if not student_record:
        return {
            "status": "error",
            "message": "Student was not found in this exam."
        }

    config = load_config()

    student_evaluation = evaluate_student_record(
        student_record,
        config
    )

    evaluated_students = []

    for record in selected_dataset.get("records", []):

        evaluated_student = evaluate_student_record(
            record,
            config
        )

        evaluated_students.append(evaluated_student)

    if not evaluated_students:
        return {
            "status": "error",
            "message": "No comparable student records were found."
        }

    total_average = 0

    for student in evaluated_students:
        total_average += student["average"]

    cohort_average = round(
        total_average / len(evaluated_students),
        2
    )

    student_average = student_evaluation["average"]

    relative_gap = round(
        student_average - cohort_average,
        2
    )

    return {
        "status": "success",
        "student_id": student_id,
        "exam_name": selected_dataset["exam_name"],
        "exam_date": selected_dataset["exam_date"],
        "student_average": student_average,
        "cohort_average": cohort_average,
        "relative_gap": relative_gap,
        "cohort_size": len(evaluated_students)
    } 
    

def analyze_cohort_performance(student_id, exam_name):

    datasets = get_all_datasets()

    selected_dataset = None

    for dataset in datasets:
        if dataset["exam_name"] == exam_name:
            selected_dataset = dataset
            break

    if not selected_dataset:
        return {
            "status": "error",
            "message": "Exam dataset was not found."
        }

    student_record = get_student_record_from_dataset(
        selected_dataset,
        student_id
    )

    if not student_record:
        return {
            "status": "error",
            "message": "Student was not found in this exam."
        }

    config = load_config()

    evaluated_students = []

    for record in selected_dataset.get("records", []):

        evaluated_student = evaluate_student_record(
            record,
            config
        )

        evaluated_students.append(evaluated_student)

    if not evaluated_students:
        return {
            "status": "error",
            "message": "No student records were found in this dataset."
        }

    averages = []

    gpas = []

    for student in evaluated_students:
        averages.append(student["average"])
        gpas.append(student["gpa"])

    mean_average = round(
        sum(averages) / len(averages),
        2
    )

    mean_gpa = round(
        sum(gpas) / len(gpas),
        2
    )

    highest_average = max(averages)
    lowest_average = min(averages)

    ranked_students = sorted(
        evaluated_students,
        key=lambda student: (
            student["average"],
            student["gpa"],
            student["total"]
        ),
        reverse=True
    )

    student_rank = None

    for rank, student in enumerate(ranked_students, start=1):

        if student["student_id"] == student_id:
            student_rank = rank
            break

    student_average = student_record["marks"]

    student_evaluation = evaluate_student_record(
        student_record,
        config
    )

    relative_gap = round(
        student_evaluation["average"] - mean_average,
        2
    )

    return {
        "status": "success",
        "student_id": student_id,
        "exam_name": selected_dataset["exam_name"],
        "exam_date": selected_dataset["exam_date"],

        "cohort_size": len(evaluated_students),

        "mean_average": mean_average,
        "highest_average": round(highest_average, 2),
        "lowest_average": round(lowest_average, 2),
        "mean_gpa": mean_gpa,

        "student_average": student_evaluation["average"],
        "student_gpa": student_evaluation["gpa"],
        "student_rank": student_rank,
        "relative_gap": relative_gap
    }  

def analyze_subject_consistency(student_id):

    performance_result = build_student_performance_series(student_id)

    if performance_result["status"] == "error":
        return performance_result

    performance_series = performance_result["performance_series"]

    if len(performance_series) < 2:
        return {
            "status": "error",
            "message": "At least 2 exam records are required for subject consistency analysis."
        }

    subjects = list(performance_series[0]["marks"].keys())

    subject_results = {}

    for subject in subjects:

        subject_marks = []

        for entry in performance_series:

            if subject in entry["marks"]:
                subject_marks.append(entry["marks"][subject])

        if len(subject_marks) < 2:
            continue

        mean_mark = round(
            sum(subject_marks) / len(subject_marks),
            2
        )

        standard_deviation = round(
            calculate_standard_deviation(subject_marks),
            2
        )

        subject_results[subject] = {
            "exam_count": len(subject_marks),
            "mean_mark": mean_mark,
            "standard_deviation": standard_deviation,
            "highest_mark": max(subject_marks),
            "lowest_mark": min(subject_marks)
        }

    if not subject_results:
        return {
            "status": "error",
            "message": "Not enough subject data was found for consistency analysis."
        }

    most_consistent_subject = min(
        subject_results,
        key=lambda subject:
        subject_results[subject]["standard_deviation"]
    )

    least_consistent_subject = max(
        subject_results,
        key=lambda subject:
        subject_results[subject]["standard_deviation"]
    )

    return {
        "status": "success",
        "student_id": student_id,
        "exam_count": len(performance_series),
        "subjects": subject_results,
        "most_consistent_subject": most_consistent_subject,
        "least_consistent_subject": least_consistent_subject
    }     















    











    
     
    
         

        
        
    


    




    
    
    
    
    

    
        





          



    
    

    








    
    





        

    

    
    












   
       
       
   
   

