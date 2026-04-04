from modules.student_manager import get_student_by_id
from modules.dataset_manager import get_all_datasets


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


    

    



