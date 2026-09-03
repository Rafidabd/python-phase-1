from modules.config_loader import load_config
from modules.analytics import evaluate_student_record
from modules.dataset_manager import get_all_datasets

from modules.intelligence.history import get_student_record_from_dataset
from modules.intelligence.performance import build_student_performance_series
from modules.intelligence.trends import (
    analyze_student_trend,
    extract_metric_changes
) 
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
 