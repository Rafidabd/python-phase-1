"""
Reusable helper functions for validation, formatting, and utilities.


""" 

from datetime import datetime

def is_valid_int(value, field_name="Value"):
    if isinstance(value, bool):
        return {
            "status": "error",
            "message": f"{field_name} must be an integer."
        }

    if not isinstance(value, int):
        return {
            "status": "error",
            "message": f"{field_name} must be an integer."
        }

    return {"status": "success"}


def is_valid_str(value, field_name="Value"):
    if not isinstance(value, str):
        return {
            "status": "error",
            "message": f"{field_name} must be a string."
        }

    if not value.strip():
        return {
            "status": "error",
            "message": f"{field_name} cannot be empty."
        }

    return {"status": "success"}


def normalize_name(name):
    cleaned_name = " ".join(name.strip().split())
    return cleaned_name.title()


def validate_board(board, config_boards):
    if board not in config_boards:
        return {
            "status": "error",
            "message": "Invalid board. Please enter a board from config."
        }

    return {"status": "success"}


def validate_student_id_uniqueness(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return {
                "status": "error",
                "message": "Student ID already exists."
            }

    return {"status": "success"}


def class_roll_uniqueness(
    students,
    institution,
    section,
    batch,
    class_roll,
    exclude_student_id=None
):
    for student in students:
        if exclude_student_id is not None and student["id"] == exclude_student_id:
            continue

        if (
            student["institution"].strip().lower() == institution.strip().lower()
            and student["section"].strip().lower() == section.strip().lower()
            and student["batch"] == batch
            and student["class_roll"] == class_roll
        ):
            return {
                "status": "error",
                "message": "Class roll already exists for this institution, section, and batch."
            }

    return {"status": "success"}


def student_finder_by_id(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def validate_subjects(marks, config_subjects):
    if not isinstance(marks, dict):
        return {
            "status": "error",
            "message": "Marks must be provided as a dictionary."
        }

    mark_subjects = set(marks.keys())
    required_subjects = set(config_subjects)

    missing_subjects = required_subjects - mark_subjects
    extra_subjects = mark_subjects - required_subjects

    if missing_subjects:
        return {
            "status": "error",
            "message": f"Missing subjects: {', '.join(sorted(missing_subjects))}."
        }

    if extra_subjects:
        return {
            "status": "error",
            "message": f"Invalid extra subjects: {', '.join(sorted(extra_subjects))}."
        }

    return {"status": "success"}   


def validate_marks_range(marks, min_mark, max_mark):
    if not isinstance(marks, dict):
        return {
            "status": "error",
            "message": "Marks must be provided as a dictionary."
        }

    for subject, mark in marks.items():
        if isinstance(mark, bool) or not isinstance(mark, (int, float)):
            return {
                "status": "error",
                "message": f"{subject} mark must be numeric."
            }

        if mark < min_mark or mark > max_mark:
            return {
                "status": "error",
                "message": f"{subject} mark must be between {min_mark} and {max_mark}."
            }

    return {"status": "success"}


def find_dataset_by_name(datasets, exam_name):
    for dataset in datasets:
        if dataset["exam_name"].strip().lower() == exam_name.strip().lower():
            return dataset
    return None 



def is_valid_exam_date(exam_date):
    if not isinstance(exam_date, str) or not exam_date.strip():
        return {
            "status": "error",
            "message": "Exam date cannot be empty."
        }

    exam_date = exam_date.strip()

    try:
        datetime.strptime(exam_date, "%Y-%m-%d")
        return {
            "status": "success"
        }
    except ValueError:
        return {
            "status": "error",
            "message": "Exam date must be in YYYY-MM-DD format and be a valid calendar date."
        } 




