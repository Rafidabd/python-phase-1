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
    performance_series=build_student_performance_series(student_id)
    student_performance_series=performance_series["performance_series"]
    if student_performance_series["status"]=="error":
        return student_performance_series
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











    


    


    



    















    











    
     
    
         

        
        
    


    




    
    
    
    
    

    
        





          



    
    

    








    
    





        

    

    
    












   
       
       
   
   

