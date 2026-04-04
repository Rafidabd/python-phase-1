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



       












   
       
       
   
   

