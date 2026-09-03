from modules.analytics import evaluate_student_record
from modules.config_loader import load_config
from modules.intelligence.history import get_student_academic_history


def build_performance_series_entry(history_entry, config):
    record = {
        "student_id": history_entry["student_id"],
        "marks": history_entry["marks"]
    }

    evaluated_student = evaluate_student_record(record, config)

    performance_series = {
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

    student_performance_series = []

    for entry in history:
        student_performance_series.append(
            build_performance_series_entry(entry, config)
        )

    return {
        "status": "success",
        "performance_series": student_performance_series
    } 