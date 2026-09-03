from modules.config_loader import load_config
from modules.analytics import classify_performance
from modules.intelligence.performance import build_student_performance_series
from modules.intelligence.trends import (
    analyze_student_trend,
    extract_metric_changes
)
from modules.intelligence.risk import get_latest_performance_entry


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
    performance_series = build_student_performance_series(student_id)

    if performance_series["status"] == "error":
      return performance_series

    student_performance_series = performance_series["performance_series"]
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
 