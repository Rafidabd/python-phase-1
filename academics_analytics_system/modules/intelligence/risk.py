from modules.config_loader import load_config
from modules.intelligence.performance import build_student_performance_series
from modules.intelligence.trends import (
    extract_metric_changes,
    analyze_student_trend
)


def get_latest_performance_entry(performance_series):
    if not performance_series:
        return None
    return performance_series[-1]


def count_declining_steps(change_list, trend_config, metric_name):
    if not change_list:
        return 0
    if metric_name not in ["average", "gpa", "weak_subject_count"]:
        return 0
    if metric_name=="average":
        decline_margin = trend_config["decline_margin"]        
        decline_count=0
        for change in change_list:
            if change<=decline_margin:
                decline_count+=1
        return decline_count
    elif metric_name=="gpa":
        decline_margin = trend_config["decline_margin"]  
        decline_count=0
        for change in change_list:
            if change<=decline_margin:
                decline_count+=1
        return decline_count
    elif metric_name=="weak_subject_count":
        decline_margin = trend_config["decline_margin"]  
        decline_count=0
        for change in change_list:
            if change>=decline_margin:
                decline_count+=1
        return decline_count
    
    
    
    
    
def build_risk_flags(latest_entry, trend_result, config):
    risk_flags = {
        "low_gpa": False,
        "high_weak_subject_burden": False,
        "declining_average_trend": False,
        "declining_gpa_trend": False,
        "worsening_weak_subject_trend": False,
        "overall_declining_trend": False,
        "repeated_decline": False
    }

    low_gpa = False
    high_weak_subject_burden = False
    declining_average_trend = False
    declining_gpa_trend = False
    worsening_weak_subject_trend = False
    overall_declining_trend = False
    repeated_decline = False

    if not latest_entry:
        return risk_flags

    min_gpa = config["risk_rules"]["min_gpa"]
    if latest_entry["gpa"] < min_gpa:
        low_gpa = True

    max_weak_subjects = config["risk_rules"]["max_weak_subjects"]
    if latest_entry["weak_subject_count"] >= max_weak_subjects:
        high_weak_subject_burden = True

    if not trend_result or trend_result["status"] == "error":
        risk_flags = {
            "low_gpa": low_gpa,
            "high_weak_subject_burden": high_weak_subject_burden,
            "declining_average_trend": declining_average_trend,
            "declining_gpa_trend": declining_gpa_trend,
            "worsening_weak_subject_trend": worsening_weak_subject_trend,
            "overall_declining_trend": overall_declining_trend,
            "repeated_decline": repeated_decline
        }
        return risk_flags

    if trend_result["average_trend"]["trend"] == "declining":
        declining_average_trend = True

    if trend_result["gpa_trend"]["trend"] == "declining":
        declining_gpa_trend = True

    if trend_result["weak_subject_trend"]["trend"] == "declining":
        worsening_weak_subject_trend = True

    if trend_result["overall_trend"] == "declining":
        overall_declining_trend = True

    trend_steps = trend_result["trend_steps"]

    average_changes = extract_metric_changes(trend_steps, "average_change")
    gpa_changes = extract_metric_changes(trend_steps, "gpa_change")
    weak_subject_changes = extract_metric_changes(trend_steps, "weak_subject_count_change")

    average_decline_count = count_declining_steps(
        average_changes,
        config["trend_thresholds"]["average"],
        "average"
    )

    gpa_decline_count = count_declining_steps(
        gpa_changes,
        config["trend_thresholds"]["gpa"],
        "gpa"
    )

    weak_subject_decline_count = count_declining_steps(
        weak_subject_changes,
        config["trend_thresholds"]["weak_subject_count"],
        "weak_subject_count"
    )

    required_decline_count = config["risk_rules"]["decline_count"]

    if average_decline_count >= required_decline_count:
        repeated_decline = True
    if gpa_decline_count >= required_decline_count:
        repeated_decline = True
    if weak_subject_decline_count >= required_decline_count:
        repeated_decline = True

    risk_flags = {
        "low_gpa": low_gpa,
        "high_weak_subject_burden": high_weak_subject_burden,
        "declining_average_trend": declining_average_trend,
        "declining_gpa_trend": declining_gpa_trend,
        "worsening_weak_subject_trend": worsening_weak_subject_trend,
        "overall_declining_trend": overall_declining_trend,
        "repeated_decline": repeated_decline
    }

    return risk_flags



def build_risk_reasons(risk_flags):
    if not risk_flags:
        return []
    reasons=[]
    if risk_flags["low_gpa"]:
        reasons.append("Latest GPA is below the minimum acceptable threshold.")
    if risk_flags["high_weak_subject_burden"]:
        reasons.append("Current weak subject burden is above the allowed limit.")
    
    if risk_flags["declining_average_trend"]:
        reasons.append("Average trend is declining across exams.")
    if risk_flags["declining_gpa_trend"]:
        reasons.append("GPA trend is declining across exams.")
    if risk_flags["worsening_weak_subject_trend"]:
        reasons.append("Weak subject burden is worsening over time.")
    if risk_flags["overall_declining_trend"]:
        reasons.append("Overall Academic Trend is declining.")
    if risk_flags["repeated_decline"]:
        reasons.append("Repeated decline has been detected across performance history.")
    return reasons 


def calculate_risk_score(risk_flags,config):
    if not risk_flags:
        return 0
    risk_score=0
    for flag_name, flag_value in risk_flags.items():
     if flag_value:
        risk_score=risk_score+ config["risk_scoring"][flag_name]
    return risk_score 



def classify_risk_level(risk_score,config):
    risk_levels=config["risk_levels"]
    for level,level_range in risk_levels.items():
        if level_range["min_score"]<=risk_score<=level_range["max_score"]:
            return level
        
    return "low" 
        

def analyze_student_risk(student_id):
    performance_result=build_student_performance_series(student_id)
    if performance_result["status"]=="error":
        return performance_result
    performance_series = performance_result["performance_series"]
    latest_entry=get_latest_performance_entry(performance_series)
    if not latest_entry:
        return {
    "status": "error",
    "message": "No performance records found for risk analysis."
           }
    config=load_config()
    
    trend_analysis=analyze_student_trend(student_id)
    risk_flags=build_risk_flags(latest_entry, trend_analysis, config)
    risk_reasons=build_risk_reasons(risk_flags)
    risk_score=calculate_risk_score(risk_flags,config)
    risk_level=classify_risk_level(risk_score,config)
    at_risk = risk_level in config["risk_policies"]["at_risk_levels"]
    
    current_snapshot={
    "average": latest_entry["average"],
    "gpa": latest_entry["gpa"],
    "weak_subject_count": latest_entry["weak_subject_count"],
    "performance": latest_entry["performance"]
        }  
    if not trend_analysis["status"]=="error":
     trend_snapshot={
     "average_trend": trend_analysis["average_trend"]["trend"],
     "gpa_trend": trend_analysis["gpa_trend"]["trend"],
     "weak_subject_trend": trend_analysis["weak_subject_trend"]["trend"],
     "overall_trend": trend_analysis["overall_trend"]
             }  
    if trend_analysis["status"]=="error":
         trend_snapshot={
            "average_trend": None,
            "gpa_trend": None,
            "weak_subject_trend": None,
            "overall_trend": None
           }
    
    final_analysis={
    "status": "success",
    "student_id": student_id,
    "latest_exam": latest_entry["exam_name"],
    "latest_exam_date": latest_entry["exam_date"],
    "current_snapshot": current_snapshot,
        
    "trend_snapshot": trend_snapshot,
    
    "risk_flags":risk_flags,
    "risk_reasons": risk_reasons,
    "risk_score": risk_score,
    "risk_level": risk_level,
    "at_risk": at_risk
        }
    

    return final_analysis 
 