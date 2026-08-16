"""
Transforms analysis results into human-readable insights.
"""
from modules.predictor import analyze_student_risk,analyze_student_trend,predict_student_performance
from modules.config_loader import load_config
def build_current_status_insight(risk_result):
    if not risk_result:
        return "Current Academic Status could not be interpreted"
    if risk_result["status"]=="error":
        
       return "Current Academic Status could not be interpreted"
    
    current_snapshot=risk_result["current_snapshot"]
    risk_flags=risk_result["risk_flags"]
    performance=current_snapshot["performance"]
    insight=""
    base_insight=""
    gpa_insight=""
    weak_subject_insight=""
    if performance=="excellent":
        base_insight="The student is currently in an excellent academic state"
    elif performance=="good":
        base_insight="The student is currently performing at a good academic level"
    elif performance=="average":
        base_insight="The student is currently performing at an average academic level"
    else:
        base_insight="The student is currently in a poor academic state"
    if risk_flags["low_gpa"]==True:
        gpa_insight="GPA below the acceptable threshold"
    else:
        gpa_insight="acceptable GPA"
    if risk_flags["high_weak_subject_burden"] == True:
        weak_subject_insight="a high weak subject burden."
    else:
        weak_subject_insight="manageable weak subject burden."

    insight=base_insight+","+" with "+gpa_insight+" and "+weak_subject_insight
    return insight



def build_trend_insight(trend_result):
    if not trend_result:
        return "Trend pattern could not be interpreted from the available exam history."
    if trend_result["status"]=="error":
        
       return "Trend pattern could not be interpreted from the available exam history."
    average_trend=trend_result["average_trend"]["trend"]
    gpa_trend=trend_result["gpa_trend"]["trend"]
    
    weak_subject_trend=trend_result["weak_subject_trend"]["trend"]
    overall_trend=trend_result["overall_trend"]
    trend_insight=""
    overall_insight=""
    supporting_insight=""
    if overall_trend=="improving":
        overall_insight="Recent exam history shows an improving academic trajectory"
    elif overall_trend=="declining":
        overall_insight="Recent exam history indicates a declining academic trajectory"
    elif overall_trend=="stable":
        overall_insight= "Recent exam history suggests a largely stable academic pattern"
    else:
        overall_insight="Recent exam history shows a mixed academic pattern"
    if overall_trend=="declining" and gpa_trend=="declining" and  weak_subject_trend=="declining":
        supporting_insight="GPA decreasing and weak-subject burden worsening over time."
    elif overall_trend=="improving" and gpa_trend=="improving" and  weak_subject_trend=="improving":
        supporting_insight="stronger GPA movement and a more manageable weak-subject burden."
    elif overall_trend=="stable":
        supporting_insight="no major directional shift dominating the profile."
    elif overall_trend=="mixed":
        supporting_insight="some metrics improving while others remain unstable."
    else:
        supporting_insight="some metrics are moving differently across recent exams."
    trend_insight=overall_insight+","+" with "+supporting_insight
    return trend_insight 



def build_risk_insight(risk_result):
    if not risk_result:
        return "Academic risk status could not be interpreted."
    if risk_result["status"] == "error":
        return "Academic risk status could not be interpreted."

    risk_level = risk_result["risk_level"]
    risk_flags = risk_result["risk_flags"]

    if risk_level == "low":
        return "The student is currently classified as low risk, with no major academic warning signal dominating the profile."

    causes = []

    if risk_flags["low_gpa"]:
        causes.append("low GPA")

    if risk_flags["high_weak_subject_burden"]:
        causes.append("high weak-subject burden")

    if risk_flags["repeated_decline"]:
        causes.append("repeated decline across performance history")

    if risk_flags["overall_declining_trend"]:
        causes.append("an overall declining trend")

    
    causes = causes[:3]

    
    if len(causes) == 1:
        cause_text = causes[0]
    elif len(causes) == 2:
        cause_text = causes[0] + " and " + causes[1]
    else:
        cause_text = causes[0] + ", " + causes[1] + ", and " + causes[2]

    if risk_level == "high":
        return "The student is currently classified as high risk due to " + cause_text + "."
    else:
        return "The student is currently classified as moderate risk due to " + cause_text + "."



def build_prediction_insight(prediction_result, config):
    if not prediction_result:
        return "Future performance prediction could not be interpreted."
    if prediction_result["status"] == "error":
        return "Future performance prediction could not be interpreted."

    predicted_metrics = prediction_result["predicted_metrics"]
    predicted_performance = prediction_result["predicted_performance"]

    predicted_gpa = predicted_metrics["gpa"]
    predicted_weak_subject_count = predicted_metrics["weak_subject_count"]

    min_gpa = config["risk_rules"]["min_gpa"]
    max_weak_subjects = config["risk_rules"]["max_weak_subjects"]

    base_insight = ""
    gpa_insight = ""
    weak_subject_insight = ""
    connector = " and "

    if predicted_performance == "excellent":
        base_insight = "The next likely performance is projected in the excellent band"
    elif predicted_performance == "good":
        base_insight = "The next likely performance is projected in the good band"
    elif predicted_performance == "average":
        base_insight = "The next likely performance is projected around the average band"
    else:
        base_insight = "The next likely performance is projected in the poor band"

    if predicted_gpa < min_gpa:
        gpa_insight = "a below-threshold GPA outlook"
    else:
        gpa_insight = "acceptable GPA expectation"

    if predicted_weak_subject_count >= max_weak_subjects:
        weak_subject_insight = "an elevated weak-subject burden"
    else:
        weak_subject_insight = "manageable weak-subject burden"

    if gpa_insight == "acceptable GPA expectation" and weak_subject_insight == "an elevated weak-subject burden":
        connector = " but "
    elif gpa_insight == "a below-threshold GPA outlook" and weak_subject_insight == "manageable weak-subject burden":
        connector = " but "

    return base_insight + ", with " + gpa_insight + connector + weak_subject_insight + "."


def extract_key_strengths(trend_result, risk_result, prediction_result):
    strengths = []

    if trend_result and trend_result["status"]!= "error":
        if trend_result["overall_trend"] == "improving":
            strengths.append("Overall academic trend is improving.")

        if trend_result["average_trend"]["trend"] == "improving":
            strengths.append("Average performance is improving across exams.")

        if trend_result["gpa_trend"]["trend"] == "improving":
            strengths.append("GPA trend is improving over time.")

        if trend_result["weak_subject_trend"]["trend"] == "improving":
            strengths.append("Weak-subject burden is becoming more manageable.")

    if risk_result and risk_result["status"] != "error":
        risk_flags = risk_result["risk_flags"]

        if risk_result["risk_level"] == "low":
            strengths.append("Current academic risk remains low.")

        if risk_flags["low_gpa"] == False:
            strengths.append("Current GPA remains within the acceptable range.")

        if risk_flags["high_weak_subject_burden"] == False:
            strengths.append("Current weak-subject burden is manageable.")

    if prediction_result and prediction_result["status"] != "error":
        predicted_metrics = prediction_result["predicted_metrics"]
        predicted_performance = prediction_result["predicted_performance"]

        if predicted_performance in ["excellent", "good"]:
            strengths.append("Predicted performance remains in the " + predicted_performance + " band.")

        if predicted_metrics["weak_subject_count"] < 2:
            strengths.append("Predicted weak-subject burden remains manageable.")

    final_strengths = []
    for strength in strengths:
        if strength not in final_strengths:
            final_strengths.append(strength)

    return final_strengths[:5]


def extract_key_concerns(trend_result, risk_result, prediction_result):
    concerns = []

    
    if trend_result and trend_result["status"] != "error":
        if trend_result["overall_trend"] == "declining":
            concerns.append("Overall academic trend is declining.")

        if trend_result["gpa_trend"]["trend"] == "declining":
            concerns.append("GPA trend is declining across exams.")

        if trend_result["average_trend"]["trend"] == "declining":
            concerns.append("Average performance is declining across exams.")

        if trend_result["weak_subject_trend"]["trend"] == "declining":
            concerns.append("Weak-subject burden is worsening over time.")

    
    if risk_result and risk_result["status"] != "error":
        for reason in risk_result["risk_reasons"]:
            if reason not in concerns:
                concerns.append(reason)

    
    if prediction_result and prediction_result["status"] != "error":
        predicted_metrics = prediction_result["predicted_metrics"]
        predicted_performance = prediction_result["predicted_performance"]

        if predicted_performance == "poor":
            concerns.append("Predicted performance remains in the poor band.")
        elif predicted_performance == "average":
            concerns.append("Predicted performance remains around the average band.")

        if predicted_metrics["gpa"] < 2.5:
            concerns.append("Predicted GPA remains below the acceptable threshold.")

        if predicted_metrics["weak_subject_count"] >= 2:
            concerns.append("Predicted weak-subject burden remains elevated.")

    
    final_concerns = []
    for concern in concerns:
        if concern not in final_concerns:
            final_concerns.append(concern)

    return final_concerns[:6]  



def extract_priority_signals(trend_result, risk_result, prediction_result,config):
    priority_signals=[]
    if not trend_result or not risk_result or not prediction_result:
        return []
    if risk_result["status"] == "error":
        return []
    if trend_result["status"] == "error":
        return []
    if prediction_result["status"] == "error":
        return []
    risk_flags = risk_result["risk_flags"]
    if risk_flags["low_gpa"]:
        priority_signals.append("Low GPA remains the strongest current risk signal.")
    if risk_flags["repeated_decline"]:
        priority_signals.append("Repeated decline across exams indicates structural academic deterioration.")
    if risk_flags["overall_declining_trend"]:
        priority_signals.append("Overall academic trend is declining.")
    if risk_flags["high_weak_subject_burden"]:
        priority_signals.append("High weak-subject burden needs immediate attention.")
    if prediction_result["predicted_performance"]=="poor":
        priority_signals.append("Predicted performance remains in the poor band.")
    if prediction_result["predicted_metrics"]["weak_subject_count"] >= config["risk_rules"]["max_weak_subjects"]:
      priority_signals.append("Predicted weak-subject burden remains elevated.")
    if prediction_result["predicted_metrics"]["gpa"]<config["risk_rules"]["min_gpa"]:
        priority_signals.append("Predicted GPA remains below the acceptable threshold.")
    if priority_signals:
     return priority_signals[:3]
    
    if trend_result["overall_trend"]=="improving":
        priority_signals.append("Overall trend is improving and remains the strongest positive signal.")
    if risk_result["risk_level"]=="low":
        priority_signals.append("Current academic risk remains low.")
    if prediction_result["predicted_performance"] in ["good", "excellent"]:
        priority_signals.append("Predicted performance remains in the " + prediction_result["predicted_performance"] + " band.")
    if prediction_result["predicted_metrics"]["weak_subject_count"] < config["risk_rules"]["max_weak_subjects"]:
     priority_signals.append("Predicted weak-subject burden remains manageable.")
    
    if not priority_signals:
        return []
    if priority_signals:
        return priority_signals[:3]
    




def build_summary_insight(trend_result, risk_result, prediction_result):
    if not trend_result or trend_result["status"] == "error":
        return "Overall academic summary could not be generated from the available analysis."
    if not risk_result or risk_result["status"] == "error":
        return "Overall academic summary could not be generated from the available analysis."
    if not prediction_result or prediction_result["status"] == "error":
        return "Overall academic summary could not be generated from the available analysis."

    risk_level = risk_result["risk_level"]
    overall_trend = trend_result["overall_trend"]
    predicted_performance = prediction_result["predicted_performance"]

    if risk_level == "high" and overall_trend == "declining" and predicted_performance in ["poor", "average"]:
        return "Overall, the student remains academically vulnerable: current risk is high, the overall trend is declining, and the predicted next state does not yet show strong recovery."

    if risk_level == "low" and overall_trend in ["improving", "stable"] and predicted_performance in ["good", "excellent"]:
        return "Overall, the student appears academically stable to improving, with manageable current risk and a favorable near-term performance outlook."

    if risk_level == "moderate" or overall_trend == "mixed":
        return "Overall, the student shows a mixed academic profile: some conditions remain manageable, but instability or moderate risk still requires attention."

    return "Overall, the student shows a developing academic profile, with current risk, trend direction, and predicted performance needing to be reviewed together."



def generate_student_insights(student_id):
    trend_result=analyze_student_trend(student_id)
    if trend_result["status"]=="error":
        return trend_result
    risk_result=analyze_student_risk(student_id)
    if risk_result["status"]=="error":
        return risk_result
    prediction_result=predict_student_performance(student_id)
    if prediction_result["status"]=="error":
        return prediction_result
    config=load_config()
    current_status_insight = build_current_status_insight(risk_result)
    trend_insight = build_trend_insight(trend_result)
    risk_insight = build_risk_insight(risk_result)
    prediction_insight = build_prediction_insight(prediction_result, config)
    summary_insight = build_summary_insight(trend_result, risk_result, prediction_result)
    key_strengths = extract_key_strengths(trend_result, risk_result, prediction_result)
    key_concerns = extract_key_concerns(trend_result, risk_result, prediction_result)
    priority_signals = extract_priority_signals(trend_result, risk_result, prediction_result, config)
    return {
    "status": "success",
    "student_id": student_id,
    "insight_sections": {
        "current_status": current_status_insight,
        "trend": trend_insight,
        "risk": risk_insight,
        "prediction": prediction_insight,
        "summary": summary_insight
    },
    "key_strengths": key_strengths,
    "key_concerns": key_concerns,
    "priority_signals": priority_signals
          } 
    

    
    
