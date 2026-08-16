from modules.storage import load_json, save_json
from modules.config_loader import load_config
from modules.student_manager import get_student_by_id
from utils.helpers import (
    find_dataset_by_name,
    is_valid_int,
    is_valid_str,
    validate_board,validate_marks_range,validate_subjects,is_valid_exam_date
)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
datasets_file_path = BASE_DIR / "data" / "datasets.json" 


def get_all_datasets():
    loaded_datasets = load_json(datasets_file_path)
    return loaded_datasets["datasets"]


def get_dataset_by_name(exam_name):
    datasets = get_all_datasets()
    dataset = find_dataset_by_name(datasets, exam_name)
    return dataset


def create_dataset(exam_name,exam_date, dataset_type, institution, board, batch):
    config = load_config()
    allowed_types = config["dataset_types"]
    allowed_boards=config["boards"]

    datasets_data = load_json(datasets_file_path)
    datasets = datasets_data["datasets"]

    name_validation = is_valid_str(exam_name, "Exam name")
    type_validation = is_valid_str(dataset_type, "Dataset type")
    batch_validation = is_valid_int(batch, "Batch")
    date_validation = is_valid_exam_date(exam_date)

    if name_validation["status"] == "error":
        return name_validation
    if type_validation["status"] == "error":
        return type_validation
    if batch_validation["status"] == "error":
        return batch_validation
    if date_validation["status"] == "error":
        return date_validation
    exam_name = exam_name.strip()
    exam_date = exam_date.strip()
    dataset_type = dataset_type.strip().lower()
    

    for dataset in datasets:
        if dataset["exam_name"].strip().lower() == exam_name.strip().lower():
            return {
                "status": "error",
                "message": "Exam name must be unique."
            }

    if dataset_type not in allowed_types:
        return {
            "status": "error",
            "message": f"{dataset_type} is not a valid dataset type."
        }

    if dataset_type == "internal":
        institution_validation = is_valid_str(institution, "Institution")
        if institution_validation["status"] == "error":
            return institution_validation

        if board not in (None, ""):
            return {
                "status": "error",
                "message": "Board must be empty for internal datasets."
            }

        institution = institution.strip()
        board = None

    elif dataset_type == "board":
        board_validation = is_valid_str(board, "Board")
        board_validation_from_config = validate_board(board, allowed_boards)
        if board_validation["status"] == "error":
            return board_validation
        if board_validation_from_config["status"] == "error":
            return board_validation_from_config
        

        if institution not in (None, ""):
            return {
                "status": "error",
                "message": "Institution must be empty for board datasets."
            }

        board = board.strip()
        institution = None

    dataset_dict = {
        "exam_name": exam_name.strip(),
        "exam_date": exam_date.strip(),
        "type": dataset_type.strip(),
        "institution": institution,
        "board": board,
        "batch": batch,
        "records": []
    }

    datasets.append(dataset_dict)
    save_json(datasets_file_path, datasets_data)

    return {
        "status": "success",
        "message": "Dataset created successfully."
    }  
                 

def add_student_record(exam_name, student_id, marks):
    loaded_datasets = load_json(datasets_file_path)
    datasets = loaded_datasets["datasets"]

    config = load_config()
    subjects = config["subjects"]
    min_mark = config["mark_limits"]["min"]
    max_mark = config["mark_limits"]["max"]

    exam_name_validation = is_valid_str(exam_name, "Exam name")
    stu_id_validation = is_valid_int(student_id, "Student id")

    if exam_name_validation["status"] == "error":
        return exam_name_validation
    if stu_id_validation["status"] == "error":
        return stu_id_validation

    dataset_search = find_dataset_by_name(datasets, exam_name)
    if not dataset_search:
        return {
            "status": "error",
            "message": "Dataset not found"
        }

    student_search = get_student_by_id(student_id)
    if not student_search:
        return {
            "status": "error",
            "message": "Student not found"
        }

    for record in dataset_search["records"]:
        if record["student_id"] == student_id:
            return {
                "status": "error",
                "message": "Student record already exists in this dataset"
            }

    subject_validation = validate_subjects(marks, subjects)
    if subject_validation["status"] == "error":
        return subject_validation

    marks_range_validation = validate_marks_range(marks, min_mark, max_mark)
    if marks_range_validation["status"] == "error":
        return marks_range_validation

    record_dict = {
        "student_id": student_id,
        "marks": marks
    }

    dataset_search["records"].append(record_dict)
    save_json(datasets_file_path, loaded_datasets)

    return {
        "status": "success",
        "message": "Student record has been added successfully"
    }  














