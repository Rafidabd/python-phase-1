from modules.config_loader import load_config
from modules.intelligence.performance import build_student_performance_series


def calculate_metric_change(previous_value, current_value):
    return current_value - previous_value


def classify_metric_trend(change, improvement_margin, decline_margin):
    if change >= improvement_margin:
        return "improving"
    elif change <= decline_margin:
        return "declining"
    else:
        return "stable"


def build_trend_steps(performance_series):
    if not performance_series or len(performance_series) < 2:
        return []

    comparisons = []

    for i in range(len(performance_series) - 1):
        previous_series = performance_series[i]
        next_series = performance_series[i + 1]

        avg_change = calculate_metric_change(
            previous_series["average"],
            next_series["average"]
        )

        gpa_change = calculate_metric_change(
            previous_series["gpa"],
            next_series["gpa"]
        )

        weak_subject_count_change = calculate_metric_change(
            previous_series["weak_subject_count"],
            next_series["weak_subject_count"]
        )

        exam_change = {
            "from_exam": previous_series["exam_name"],
            "to_exam": next_series["exam_name"],
            "from_date": previous_series["exam_date"],
            "to_date": next_series["exam_date"],
            "average_change": avg_change,
            "gpa_change": gpa_change,
            "weak_subject_count_change": weak_subject_count_change
        }

        comparisons.append(exam_change)

    return comparisons


def extract_metric_changes(trend_steps, metric_name):
    if not trend_steps:
        return []

    valid_metrics = [
        "average_change",
        "gpa_change",
        "weak_subject_count_change"
    ]

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


def determine_overall_trend(
    average_trend,
    gpa_trend,
    weak_subject_trend
):
    if not average_trend:
        return "mixed"

    if not gpa_trend:
        return "mixed"

    if not weak_subject_trend:
        return "mixed"

    trend_labels = [
        average_trend["trend"],
        gpa_trend["trend"],
        weak_subject_trend["trend"]
    ]

    if trend_labels[0] == trend_labels[1] == trend_labels[2]:
        return trend_labels[0]

    elif trend_labels.count("improving") == 2:
        return "improving"

    elif trend_labels.count("declining") == 2:
        return "declining"

    elif trend_labels.count("stable") == 2:
        return "stable"

    elif trend_labels.count("mixed") == 2:
        return "mixed"

    else:
        return "mixed"


def analyze_student_trend(student_id):
    result = build_student_performance_series(student_id)

    if result["status"] == "error":
        return result

    performance_series = result["performance_series"]

    if len(performance_series) < 2:
        return {
            "status": "error",
            "message": "At least 2 exam records are required for trend analysis."
        }

    config = load_config()
    trend_config = config["trend_thresholds"]

    trend_steps = build_trend_steps(performance_series)

    average_changes = extract_metric_changes(
        trend_steps,
        "average_change"
    )

    gpa_changes = extract_metric_changes(
        trend_steps,
        "gpa_change"
    )

    weak_subject_changes = extract_metric_changes(
        trend_steps,
        "weak_subject_count_change"
    )

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