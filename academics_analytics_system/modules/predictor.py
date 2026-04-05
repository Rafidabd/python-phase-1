from modules.student_manager import get_student_by_id
from modules.dataset_manager import get_all_datasets
from modules.analytics import evaluate_student_record
from modules.config_loader import load_config

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
    
    
    
    








    
    





        

    

    
    












   
       
       
   
   

