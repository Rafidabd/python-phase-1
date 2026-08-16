"""
Handles output formatting and structured terminal display.
"""

def show_main_menu():
     print("\n1.Student Management")
     print("2.Dataset Management")
     print("3.View Data")
     print("4.Analytics")
     print("5.Academic Intelligence")
     print("6.Exit")
     



def show_student_menu():
     print("\n1.Add Student")
     print("2.Update Student")
     print("3.Delete Student")
     print("4.Back to Main Menu")
     


def show_dataset_menu():
     print("\n1.Create Dataset")
     print("2.Add Student Record")
     print("3.Back to Main Menu")
 

def show_view_menu():
     print("\n1.View All Students")
     print("2.View Student by ID")
     print("3.View All Datasets")
     print("4.View Dataset by Name")
     print("5.Back to Main Menu")  

def show_academic_intelligence_menu():
    print("=" * 50)
    print("ACADEMIC INTELLIGENCE MENU".center(50))
    print("=" * 50)
    print("1. View Student Academic History")
    print("2. View Student Performance Series")
    print("3. Analyze Student Trend")
    print("4. Analyze Student Risk")
    print("5. Predict Student Performance")
    print("6. Generate Full Student Insights")
    print("7. Back")

def show_message(result):
    if result["status"] == "success":
        print(f"Success: {result['message']}")
    else:
        print(f"Error: {result['message']}")


def display_student(student):
    if not student:
        print("Error. Student not found")
    else:
        print("STUDENT'S INDIVIDUAL INFORMATION")
        print("-" * 40)
        print()
        print(f"{'ID':<20}: {student['id']}")
        print(f"{'Name':<20}: {student['name']}")
        print(f"{'Institution':<20}: {student['institution']}")
        print(f"{'Section':<20}: {student['section']}")
        print(f"{'Board':<20}: {student['board']}")
        print(f"{'Batch':<20}: {student['batch']}")
        print(f"{'Class Roll':<20}: {student['class_roll']}")

        board_roll = student["board_roll"] if student["board_roll"] is not None else "N/A"
        board_registration = student["board_registration"] if student["board_registration"] is not None else "N/A"

        print(f"{'Board Roll':<20}: {board_roll}")
        print(f"{'Board Registration':<20}: {board_registration}")
        print()


def display_all_students(students):
    if not students:
        print("Error.No student found")
        return

    for student in students:
        print("-" * 40)
        display_student(student)
    print()


def display_dataset(dataset):
    if not dataset:
        print("Error.Dataset not found")
    else:
        institution = dataset["institution"] if dataset["institution"] is not None else "N/A"
        board = dataset["board"] if dataset["board"] is not None else "N/A"

        print("DATASET INFORMATION")
        print("-" * 40)
        print()
        print(f"{'Exam Name':<20}: {dataset['exam_name']}")
        print(f"{'Type':<20}: {dataset['type']}")
        print(f"{'Institution':<20}: {institution}")
        print(f"{'Board':<20}: {board}")
        print(f"{'Batch':<20}: {dataset['batch']}")
        print(f"{'Total Records':<20}: {len(dataset['records'])}")
        print()

        print("Records:")
        print("-" * 40)

        if not dataset["records"]:
            print("No records have been added")
        else:
            for record in dataset["records"]:
                print(f"  Student ID: {record['student_id']}")
                for subject, mark in record["marks"].items():
                    print(f"    {subject:<15}: {mark}")
        print()


def display_all_datasets(datasets):
    if not datasets:
        print("Error. No dataset found")
        return

    for dataset in datasets:
        institution = dataset["institution"] if dataset["institution"] is not None else "N/A"
        board = dataset["board"] if dataset["board"] is not None else "N/A"

        print("-" * 40)
        print(f"{'Exam Name':<20}: {dataset['exam_name']}")
        print(f"{'Type':<20}: {dataset['type']}")
        print(f"{'Institution':<20}: {institution}")
        print(f"{'Board':<20}: {board}")
        print(f"{'Batch':<20}: {dataset['batch']}")
        print(f"{'Record Count':<20}: {len(dataset['records'])}")
        print()


def display_dataset_statistics(statistics):
    if not statistics:
        print("No Dataset Statistics available")
        return
    print("==========Dataset Statistics==========")
    print("-" * 40)
    print(f"{'Total Students':<20}: {statistics['student_count']}")
    print(f"{'Mean Total Marks':<20}: {statistics['dataset_mean_total']}")
    print(f"{'Mean Average Marks':<20}: {statistics['dataset_mean_average']}")
    print(f"{'Mean GPA':<20}: {statistics['mean_gpa']}")
    print(f"{'Highest Total':<20}: {statistics['highest_total']}")
    print(f"{'Lowest Total':<20}: {statistics['lowest_total']}")
    print()
    
 

def display_subject_averages(subject_averages):
    if not subject_averages:
        print("No Subject average data available")
        return
    print("==========Subject Averages==========")
    print("-" * 40)
    for subject,mark in subject_averages.items():
        print(f"{subject:<20}: {mark}")

        
    print()



def display_single_subject_insight(title,subject_name):
    if not subject_name:
        print(f"{title:<20}: {'Not Available'}")
        print()
        return

    print(f"{title:<20}: {subject_name}")
    print()



def display_student_evaluation(student_record):
    if not student_record:
        print("No Student Record Available")
        return
    print("--- Student Evaluation ---")
     
    
    print()
    print(f"{'Student ID':<20}: {student_record['student_id']}")
    print(f"{'Total Marks':<20}: {student_record['total']}")
    print(f"{'Average Marks':<20}: {student_record['average']}")
    print(f"{'GPA':<20}: {student_record['gpa']}") 
    print(f"{'Performance':<20}: {student_record['performance']}")
    print(f"{'Strongest Subject':<20}: {student_record['strongest_subject']}")
    print(f"{'Weakest Subject':<20}: {student_record['weakest_subject']}")
    print(f"{'Weak Subject Count':<20}: {student_record['weak_subject_count']}") 
    weak_subjects = student_record["weak_subjects"]
    weak_subjects_string = ", ".join(weak_subjects) if weak_subjects else "None"
    
    print(f"{'Weak Subjects':<20}: {weak_subjects_string}") 
    print()
    print("--- Subject Grades ---")
    for subject,status in student_record["subject_grades"].items():
        print(f"{subject:<20}: {status['grade']} (GPA: {status['gpa']})")
    print() 

    

def display_ranked_students(ranked_students):
    if not ranked_students:
        print("No Ranking data available")
        return
    else:
         print("--- Ranked Students ---")
         print()
         print(f"{'Rank':>6} {'Student ID':>8} {'Total':>8} {'Average':>8} {'GPA':>8} {'Performance':<20} ") 
         print("---------------------------------------------")
         for student in ranked_students:
             stu_rank=student["rank"]
             sid=student["student_id"]
             total=student["total"]
             average=student["average"]
             gpa=student["gpa"]
             performance=student["performance"]
             print(f"{stu_rank:>6} {sid:>8} {total:>8} {average:>8} {gpa:>8} {performance:<20} ") 
         print() 


def display_weak_students(weak_students):
    if not weak_students:
        print("No Weak student found")
        return
    else:
         print("--- Weak Students ---")
         print()
         print(f"{'Student ID':>8} {'Average':>8} {'GPA':>8} {'Weak Subject Count':>20} {'Performance':<20} ") 
         print("---------------------------------------------")
         for student in weak_students:
             
             sid=student["student_id"]
             average=student["average"]
             gpa=student["gpa"]
             weak_subj_count=student["weak_subject_count"]
             performance=student["performance"]
             print(f"{sid:>8} {average:>8} {gpa:>8} {weak_subj_count:>20} {performance:<20} ") 
             weak_subjects = student["weak_subjects"]
             weak_subjects_string = ", ".join(weak_subjects) if weak_subjects else "None"
             weak_subjects_string = ", ".join(weak_subjects)
             print(f"{'Weak Subjects':<20}: {weak_subjects_string}") 

         print() 


def display_student_academic_history(result):
    if not result:
        print("No academic history found.")
        return

    if result["status"] == "error":
        print(result["message"])
        return

    history = result.get("history", [])

    if not history:
        print("No academic history found.")
        return

    student_id = history[0].get("student_id", "N/A")

    print("=" * 50)
    print("STUDENT ACADEMIC HISTORY".center(50))
    print("=" * 50)

    print(f"\nStudent ID: {student_id}")
    print(f"Total Exams Found: {len(history)}")

    for index, entry in enumerate(history, start=1):
        exam_name = entry.get("exam_name", "N/A")
        exam_date = entry.get("exam_date", "N/A")
        dataset_type = entry.get("dataset_type", "N/A")
        institution = entry.get("institution") or "N/A"
        board = entry.get("board") or "N/A"
        batch = entry.get("batch", "N/A")
        marks = entry.get("marks", {})

        print("\n" + "-" * 40)
        print(f"Exam {index}: {exam_name}")
        print("-" * 40)

        print(f"{'Date':<12}: {exam_date}")
        print(f"{'Type':<12}: {dataset_type}")
        print(f"{'Institution':<12}: {institution}")
        print(f"{'Board':<12}: {board}")
        print(f"{'Batch':<12}: {batch}")

        print("\nMarks:")

        if not marks:
            print("No marks found.")
        else:
            for subject, mark in marks.items():
                print(f"{subject:<12}: {mark}") 
    


def display_student_performance_series(result):
    if not result:
        print("No performance series found.")
        return

    if result["status"] == "error":
        print(result["message"])
        return

    performance_series = result.get("performance_series", [])

    if not performance_series:
        print("No performance series found.")
        return

    student_id = performance_series[0].get("student_id", "N/A")

    print("=" * 50)
    print("STUDENT PERFORMANCE SERIES".center(50))
    print("=" * 50)

    print(f"\nStudent ID: {student_id}")
    print(f"Total Evaluated Exams: {len(performance_series)}")

    for index, entry in enumerate(performance_series, start=1):
        exam_name = entry.get("exam_name", "N/A")
        exam_date = entry.get("exam_date", "N/A")
        dataset_type = entry.get("dataset_type", "N/A")
        total = entry.get("total", "N/A")
        gpa = entry.get("gpa", "N/A")
        average = entry.get("average", "N/A")
        performance = entry.get("performance", "N/A")
        strongest_subject = entry.get("strongest_subject", "N/A")
        weakest_subject = entry.get("weakest_subject", "N/A")
        weak_subjects = entry.get("weak_subjects", [])
        weak_subjects_text = ", ".join(weak_subjects) if weak_subjects else "None"

        print("\n" + "-" * 40)
        print(f"Exam {index}: {exam_name}")
        print("-" * 40)

        print(f"{'Date':<20}: {exam_date}")
        print(f"{'Type':<20}: {dataset_type}")
        print(f"{'Total Marks':<20}: {total}")
        print(f"{'Average':<20}: {average}")
        print(f"{'GPA':<20}: {gpa}")
        print(f"{'Performance':<20}: {performance}")
        print(f"{'Strongest Subject':<20}: {strongest_subject}")
        print(f"{'Weakest Subject':<20}: {weakest_subject}")
        print(f"{'Weak Subjects':<20}: {weak_subjects_text}")
    

def format_change(value):
    if isinstance(value, (int, float)) and value > 0:
        return f"+{value}"
    return value


def display_student_trend(result):
    if not result:
        print("No trend result found.")
        return

    if result["status"] == "error":
        print(result["message"])
        return

    student_id = result.get("student_id", "N/A")
    overall_trend = result.get("overall_trend", "N/A")
    trend_steps = result.get("trend_steps", [])

    average_trend_summary = result.get("average_trend", {}).get("trend", "N/A")
    gpa_trend_summary = result.get("gpa_trend", {}).get("trend", "N/A")
    weak_subject_trend_summary = result.get("weak_subject_trend", {}).get("trend", "N/A")

    if not trend_steps:
        print("No trend steps available.")
        return

    print("=" * 50)
    print("STUDENT TREND ANALYSIS".center(50))
    print("=" * 50)

    print(f"\n{'Student ID':<25}: {student_id}")
    print(f"{'Overall Trend':<25}: {overall_trend}")

    for index, step in enumerate(trend_steps, start=1):
        from_exam = step.get("from_exam", "N/A")
        to_exam = step.get("to_exam", "N/A")
        from_date = step.get("from_date", "N/A")
        to_date = step.get("to_date", "N/A")

        average_change = format_change(step.get("average_change", "N/A"))
        gpa_change = format_change(step.get("gpa_change", "N/A"))
        weak_subject_count_change = format_change(step.get("weak_subject_count_change", "N/A"))

        print("\n" + "-" * 50)
        print(f"Trend Step {index}: {from_exam} → {to_exam}")
        print("-" * 50)

        print(f"{'From Date':<30}: {from_date}")
        print(f"{'To Date':<30}: {to_date}")
        print(f"{'Average Change':<30}: {average_change}")
        print(f"{'GPA Change':<30}: {gpa_change}")
        print(f"{'Weak Subject Count Change':<30}: {weak_subject_count_change}")

    print("\n" + "-" * 50)
    print("Metric Trend Summary")
    print("-" * 50)

    print(f"{'Average Trend':<30}: {average_trend_summary}")
    print(f"{'GPA Trend':<30}: {gpa_trend_summary}")
    print(f"{'Weak Subject Trend':<30}: {weak_subject_trend_summary}")
    print(f"{'Overall Trend':<30}: {overall_trend}")
    
    

    


    


def display_student_risk(result):
     if not result:
        print("No risk result found.")
        return

     if result["status"] == "error":
        print(result["message"])
        return
     student_id = result.get("student_id", "N/A")
     at_risk = "Yes" if result.get("at_risk", False) else "No"
     risk_level = result.get("risk_level", "N/A")
     risk_score = result.get("risk_score", "N/A")
     risk_flags = result.get("risk_flags", {})
     risk_reasons = result.get("risk_reasons", [])
     trend_snapshot = result.get("trend_snapshot", {})
     current_snapshot=result.get("current_snapshot",{})
     print("=" * 50)
     print("STUDENT RISK ANALYSIS".center(50))
     print("=" * 50)
     print()
     print(f"{'Student ID':<25}: {student_id}")
     print(f"{'At Risk':<25}: {at_risk}")
     print(f"{'Risk Level':<25}: {risk_level}")
     print(f"{'Risk Score':<25}: {risk_score}")
     print()
     print("-" * 50)
     print("Current Academic Snapshot".center(50))
     print("-" * 50)
     exam_name = result.get("latest_exam", "N/A")
     exam_date = result.get("latest_exam_date", "N/A")
     average=current_snapshot.get("average","N/A")
     gpa=current_snapshot.get("gpa","N/A")
     weak_subjects=current_snapshot.get("weak_subject_count","N/A")
     performance=current_snapshot.get("performance","N/A")
     print(f"{'Exam Name':<25}: {exam_name}")
     print(f"{'Exam Date':<25}: {exam_date}")
     print(f"{'Average':<25}: {average}")
     print(f"{'GPA':<25}: {gpa}")
     print(f"{'Weak Subjects':<25}: {weak_subjects}")
     print(f"{'Performance':<25}: {performance}")
     print()
     print("-" * 50)
     print("Trend Snapshot".center(50))
     print("-" * 50)
     overall_trend=trend_snapshot.get("overall_trend","N/A")
     average_trend=trend_snapshot.get("average_trend","N/A")
     gpa_trend=trend_snapshot.get("gpa_trend","N/A")
     weak_subject_trend=trend_snapshot.get("weak_subject_trend","N/A")
     print(f"{'Overall Trend':<25}: {overall_trend}")
     print(f"{'Average Trend':<25}: {average_trend}")
     print(f"{'GPA Trend':<25}: {gpa_trend}")
     print(f"{'Weak Subject Trend':<25}: {weak_subject_trend}")
     print()
     print("-" * 50)
     print("Risk Flags".center(50))
     print("-" * 50)
     for risk_name, risk_status in risk_flags.items():
       label = risk_name.replace("_", " ").title()
       status = "Yes" if risk_status else "No"
       print(f"{label:<35}: {status}") 
     print()
     print("-" * 50)
     print("Risk Reasons".center(50))
     print("-" * 50)
     if not risk_reasons:
      print("No major risk reasons found.")
     else:
       for index, entry in enumerate(risk_reasons, start=1):
         print(f"{index}. {entry}")
     print() 



def display_student_prediction(result):
    if not result:
        print("No prediction data found.")
        return

    if result["status"] == "error":
        print(result["message"])
        return

    student_id = result.get("student_id", "N/A")
    prediction_basis = result.get("prediction_basis", {})
    predicted_metrics = result.get("predicted_metrics", {})
    predicted_performance = result.get("predicted_performance", "N/A")
    prediction_components = result.get("prediction_components", {})

    print("=" * 50)
    print("STUDENT PERFORMANCE PREDICTION".center(50))
    print("=" * 50)
    print()

    print(f"{'Student ID':<30}: {student_id}")
    print(f"{'Predicted Average':<30}: {predicted_metrics.get('average', 'N/A')}")
    print(f"{'Predicted GPA':<30}: {predicted_metrics.get('gpa', 'N/A')}")
    print(f"{'Predicted Weak Subject Count':<30}: {predicted_metrics.get('weak_subject_count', 'N/A')}")
    print(f"{'Predicted Performance':<30}: {predicted_performance}")

    print()
    print("-" * 50)
    print("Prediction Basis".center(50))
    print("-" * 50)
    print()

    print(f"{'Recent Exam':<30}: {prediction_basis.get('recent_exam', 'N/A')}")
    print(f"{'Recent Exam Date':<30}: {prediction_basis.get('recent_exam_date', 'N/A')}")
    print(f"{'History Count':<30}: {prediction_basis.get('history_count', 'N/A')}")

    print()
    print("-" * 50)
    print("Prediction Components".center(50))
    print("-" * 50)
    print()

    if not prediction_components:
        print("No prediction components available.")
    else:
        for component_name, component_data in prediction_components.items():
            print(component_name.replace("_", " ").title())
            print(f"{'Recent Value':<30}: {component_data.get('recent_value', 'N/A')}")
            print(f"{'Historical Mean':<30}: {component_data.get('historical_mean', 'N/A')}")
            trend_mean_change = format_change(component_data.get("trend_mean_change", "N/A"))
            print(f"{'Trend Mean Change':<30}: {trend_mean_change}")
            print()

    print("Note: This prediction is heuristic-based and depends on previous exam trends.")
    print() 

            


    


def display_student_insights(result):
    if not result:
        print("No student insight data found.")
        return

    if result["status"] == "error":
        print(result["message"])
        return

    student_id = result.get("student_id", "N/A")
    insight_sections = result.get("insight_sections", {})
    key_strengths = result.get("key_strengths", [])
    key_concerns = result.get("key_concerns", [])
    priority_signals = result.get("priority_signals", [])

    print("=" * 50)
    print("STUDENT FULL INSIGHTS".center(50))
    print("=" * 50)
    print()
    print(f"{'Student ID':<20}: {student_id}")

    print()
    print("-" * 50)
    print("Current Status".center(50))
    print("-" * 50)
    print(insight_sections.get("current_status", "No current status insight available."))

    print()
    print("-" * 50)
    print("Trend Insight".center(50))
    print("-" * 50)
    print(insight_sections.get("trend", "No trend insight available."))

    print()
    print("-" * 50)
    print("Risk Insight".center(50))
    print("-" * 50)
    print(insight_sections.get("risk", "No risk insight available."))

    print()
    print("-" * 50)
    print("Prediction Insight".center(50))
    print("-" * 50)
    print(insight_sections.get("prediction", "No prediction insight available."))

    print()
    print("-" * 50)
    print("Summary".center(50))
    print("-" * 50)
    print(insight_sections.get("summary", "No summary insight available."))

    print()
    print("-" * 50)
    print("Key Strengths".center(50))
    print("-" * 50)

    if not key_strengths:
        print("No key strengths found.")
    else:
        for index, strength in enumerate(key_strengths, start=1):
            print(f"{index}. {strength}")

    print()
    print("-" * 50)
    print("Key Concerns".center(50))
    print("-" * 50)

    if not key_concerns:
        print("No key concerns found.")
    else:
        for index, concern in enumerate(key_concerns, start=1):
            print(f"{index}. {concern}")

    print()
    print("-" * 50)
    print("Priority Signals".center(50))
    print("-" * 50)

    if not priority_signals:
        print("No priority signals found.")
    else:
        for index, signal in enumerate(priority_signals, start=1):
            print(f"{index}. {signal}")

    print() 




    



    

    











        


    
    

    
    


     



     


          
          
    
    
     
     


          
          
     


     




