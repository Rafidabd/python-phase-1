"""
Handles analytical computations:
- GPA calculation
- ranking
- trends
- subject analysis
- comparisons
"""
def calculate_total(marks_dict):
    if not marks_dict:
        return 0

    total = 0
    for mark in marks_dict.values():
        total += mark
    return total


def calculate_average(marks_dict):
    if not marks_dict:
        return 0

    total = calculate_total(marks_dict)
    return round(total / len(marks_dict), 2)


def get_grade_info(mark, grading_scale):
    for grade_band in grading_scale:
        if mark >= grade_band["min"]:
            return {
                "grade": grade_band["grade"],
                "gpa": grade_band["gpa"]
            }

    return {
        "grade": "Unknown",
        "gpa": 0.0
    }


def calculate_gpa(marks_dict, grading_scale):
    if not marks_dict:
        return 0

    total_gpa = 0
    for mark in marks_dict.values():
        grade_info = get_grade_info(mark, grading_scale)
        total_gpa += grade_info["gpa"]

    return round(total_gpa / len(marks_dict), 2) 



def get_strongest_subject(marks_dict):
    if not marks_dict:
        return None
    return max(marks_dict, key=marks_dict.get)


def get_weakest_subject(marks_dict):
    if not marks_dict:
        return None
    return min(marks_dict, key=marks_dict.get)


def get_weak_subjects(marks_dict, weak_subject_mark):
    if not marks_dict:
        return []

    weak_subjects = []
    for subject, mark in marks_dict.items():
        if mark < weak_subject_mark:
            weak_subjects.append(subject)

    return weak_subjects


def classify_performance(average, performance_levels):
    sorted_levels = sorted(
        performance_levels.items(),
        key=lambda item: item[1],
        reverse=True
     )

    for performance, threshold in sorted_levels:
        if average >=threshold:
            return performance

    return "unknown"


def evaluate_student_record(record, config):
    marks = record["marks"]
    grading_scale = config["grading_scale"]
    performance_levels = config["performance_levels"]
    weak_subject_mark = config["risk_rules"]["weak_subject_mark"]

    total = calculate_total(marks)
    average = calculate_average(marks)
    gpa = calculate_gpa(marks, grading_scale)
    strongest_subject = get_strongest_subject(marks)
    weakest_subject = get_weakest_subject(marks)
    weak_subjects = get_weak_subjects(marks, weak_subject_mark)
    performance = classify_performance(average, performance_levels)

    subject_grades = {}
    for subject, mark in marks.items():
        subject_grades[subject] = get_grade_info(mark, grading_scale)

    student_record = {
        "student_id": record["student_id"],
        "marks": marks,
        "total": total,
        "average": average,
        "gpa": gpa,
        "subject_grades": subject_grades,
        "strongest_subject": strongest_subject,
        "weakest_subject": weakest_subject,
        "weak_subjects": weak_subjects,
        "weak_subject_count": len(weak_subjects),
        "performance": performance
    }

    return student_record 


def evaluate_dataset_records(dataset, config):
    if not dataset:
        return []

    evaluated_students = []
    for record in dataset.get("records", []):
        evaluated_students.append(evaluate_student_record(record, config))

    return evaluated_students


def rank_students(dataset, config):
    if not dataset:
        return []

    evaluated_students = evaluate_dataset_records(dataset, config)

    primary_criteria = config["ranking_criteria"]["primary"]
    secondary_criteria = config["ranking_criteria"]["secondary"]
    tertiary_criteria = config["ranking_criteria"]["tertiary"]

    sorted_students = sorted(
        evaluated_students,
        key=lambda student: (
            student[primary_criteria],
            student[secondary_criteria],
            student[tertiary_criteria]
        ),
        reverse=True
    )

    final_rank = []
    for rank, stu_dict in enumerate(sorted_students, start=1):
        ranked_student = stu_dict.copy()
        ranked_student["rank"] = rank
        final_rank.append(ranked_student)

    return final_rank


def get_topper(dataset, config):
    ranking_list = rank_students(dataset, config)
    if not ranking_list:
        return None
    return ranking_list[0]


def get_lowest_performer(dataset, config):
    ranking_list = rank_students(dataset, config)
    if not ranking_list:
        return None
    return ranking_list[-1]


def get_weak_students(dataset, config):
    evaluated_students = evaluate_dataset_records(dataset, config)
    min_gpa = config["risk_rules"]["min_gpa"]
    max_weak_subjects = config["risk_rules"]["max_weak_subjects"]

    weak_stu_list = []
    for student in evaluated_students:
        if student["gpa"] < min_gpa or student["weak_subject_count"] >= max_weak_subjects:
            weak_stu_list.append(student)

    return weak_stu_list 
             
         
    

def get_dataset_statistics(dataset, config):
    evaluated_students = evaluate_dataset_records(dataset, config)

    if not evaluated_students:
        return {
            "student_count": 0,
            "dataset_mean_total": 0,
            "dataset_mean_average": 0,
            "mean_gpa": 0,
            "highest_total": 0,
            "lowest_total": 0
         }

    total_students = len(evaluated_students)

    overall_total = 0
    overall_average = 0
    overall_gpa = 0

    for student in evaluated_students:
        overall_total += student["total"]
        overall_average += student["average"]
        overall_gpa += student["gpa"]

    mean_total = round(overall_total / total_students, 2)
    mean_average = round(overall_average / total_students, 2)
    mean_gpa = round(overall_gpa / total_students, 2)

    totals = [student["total"] for student in evaluated_students]
    highest_total = max(totals)
    lowest_total = min(totals)

    dataset_statistics = {
        "student_count": total_students,
        "dataset_mean_total": mean_total,
        "dataset_mean_average": mean_average,
        "mean_gpa": mean_gpa,
        "highest_total": highest_total,
        "lowest_total": lowest_total
    }

    return dataset_statistics


def get_subject_averages(dataset):
    records = dataset.get("records", [])
    if not records:
        return {}

    subjects = records[0]["marks"].keys()
    subject_totals = {}

    for subject in subjects:
        subject_totals[subject] = 0

    for record in records:
        for subject, mark in record["marks"].items():
            subject_totals[subject] += mark

    total_record = len(records)
    subject_averages = {}

    for subject, total in subject_totals.items():
        subject_averages[subject] = round(total / total_record, 2)

    return subject_averages


def get_strongest_subject_overall(dataset):
    subject_averages = get_subject_averages(dataset)
    if not subject_averages:
        return None
    return max(subject_averages, key=subject_averages.get)


def get_weakest_subject_overall(dataset):
    subject_averages = get_subject_averages(dataset)
    if not subject_averages:
        return None
    return min(subject_averages, key=subject_averages.get) 


        





    
      

         
   
    