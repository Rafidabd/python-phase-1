"""
Handles output formatting and structured terminal display.
"""

def show_main_menu():
     print("\n1.Student Management")
     print("2.Dataset Management")
     print("3.View Data")
     print("4.Analytics")
     print("5.Exit")
     



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










        


    
    

    
    


     



     


          
          
    
    
     
     


          
          
     


     




