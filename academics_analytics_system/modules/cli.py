from modules.display import show_main_menu,show_dataset_menu,show_student_menu,show_view_menu,show_message,display_student,display_all_students,display_dataset,display_all_datasets
from modules.student_manager import add_student,update_student,delete_student,get_all_students
from modules.dataset_manager import create_dataset,add_student_record,get_all_datasets,get_student_by_id,get_dataset_by_name
from modules.config_loader import load_config
from modules.analytics import (
    rank_students,
    get_topper,
    get_lowest_performer,
    get_weak_students,
    get_dataset_statistics,
    get_subject_averages,
    get_strongest_subject_overall,
    get_weakest_subject_overall,
    evaluate_student_record
)
from modules.predictor import (
    get_student_academic_history,
    build_student_performance_series,
    analyze_student_trend,
    analyze_student_risk,
    predict_student_performance,
    
)
from modules.insights import generate_student_insights

from modules.display import (
    display_student_academic_history,
    display_student_performance_series,
    display_student_trend,
    display_student_risk,
    display_student_prediction,
    display_student_insights,show_academic_intelligence_menu
)

from modules.display import (
    show_message,
    display_ranked_students,
    display_dataset_statistics,
    display_subject_averages,
    display_single_subject_insight,
    display_weak_students,
    display_student_evaluation
)
def student_menu():
    while True:
        show_student_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
             try:
              sid=int(input("ID: ").strip())
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             
             name=input("Name: ").strip()
             institution=input("Institution: ").strip() 
             section=input("Section: ").strip()
             board=input("Board: ").strip()
             try:
              batch=int(input("Batch: ").strip())
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             try:
              class_roll=int(input("Class Roll: ").strip())
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             try:

              board_roll_input = input("Board Roll: ").strip() 
              if board_roll_input == "":
                board_roll = None
              else:
                board_roll = int(board_roll_input) 
             
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             try:
              board_registration_input = input("Board Registration: ").strip()
              if board_registration_input == "":
                board_registration = None
              else:
                board_registration = int(board_registration_input) 
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             adding_student_result=add_student(sid,name,institution,section,board,batch,class_roll,board_roll,board_registration)
             show_message(adding_student_result)
             





             

            
        elif choice == "2":
             try:
              sid=int(input("ID: ").strip())
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             name=input("Name: ").strip()
             institution=input("Institution: ").strip() 
             section=input("Section: ").strip()
             board=input("Board: ").strip()
             try:
              batch=int(input("Batch: ").strip())
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             try:
              class_roll=int(input("Class Roll: ").strip())
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             try:

              board_roll_input = input("Board Roll: ").strip()
              if board_roll_input == "":
                board_roll = None
              else:
                board_roll = int(board_roll_input) 
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             try:
              board_registration_input = input("Board Registration: ").strip()
              if board_registration_input == "":
                board_registration = None
              else:
                board_registration = int(board_registration_input) 
             except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
             updating_student_result=update_student(sid,name,institution,section,board,batch,class_roll,board_roll,board_registration)
             show_message(updating_student_result)
            
             
             
             
             



            
        elif choice == "3":
           try:
              sid = int(input("ID: ").strip()) 
           except ValueError:
                 print("Invalid Value.Please Enter an Integer Value")
                 continue
           deleting_student_result=delete_student(sid)
           show_message(deleting_student_result)
           
            
        elif choice == "4":
            break
        else:
            print("Invalid choice")












def dataset_menu():
    while True:
        show_dataset_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            exam_name = input("Exam Name: ").strip()
            exam_date = input("Exam Date (YYYY-MM-DD): ").strip()
            dataset_type = input("Dataset Type: ").strip().lower()

            try:
                batch = int(input("Batch: ").strip())
            except ValueError:
                print("Invalid value. Please enter an integer.")
                continue

            if dataset_type == "internal":
                institution = input("Institution: ").strip()
                board = None
            elif dataset_type == "board":
                board = input("Board: ").strip()
                institution = None
            else:
                print("Invalid dataset type. Use internal or board.")
                continue

            creating_dataset = create_dataset(exam_name, exam_date, dataset_type, institution, board, batch)
            show_message(creating_dataset)

        elif choice == "2":
            config = load_config()
            exam_name = input("Exam Name: ").strip()

            try:
                sid = int(input("ID: ").strip())
            except ValueError:
                print("Invalid value. Please enter an integer.")
                continue

            marks_dict = {}
            invalid_marks = False

            for subject in config["subjects"]:
                try:
                    mark = int(input(f"{subject} mark: ").strip())
                except ValueError:
                    print("Invalid input. Mark must be a number.")
                    invalid_marks = True
                    break

                marks_dict[subject] = mark

            if invalid_marks:
                continue

            adding_student_record = add_student_record(exam_name, sid, marks_dict)
            show_message(adding_student_record)

        elif choice == "3":
            break

        else:
            print("Invalid choice")



def view_menu():
    while True:
        show_view_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            all_students=get_all_students()
            display_all_students(all_students)
        elif choice == "2":
            try:
           
             sid=int(input("Student ID:").strip())
            except ValueError:
               print("Error.ID Must be an integer")
               continue
            student_info=get_student_by_id(sid)
            display_student(student_info)
            
        elif choice == "3":
            datasets=get_all_datasets()
            display_all_datasets(datasets)
        elif choice == "4":
            exam_name=input("Exam Name:").strip()
            dataset=get_dataset_by_name(exam_name)
            display_dataset(dataset) 
        elif choice == "5":
            break
        else:
            print("Invalid choice")


def get_dataset_input():
    exam_name = input("Enter dataset/exam name: ")
    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        print("Dataset not found.")
        return None

    return dataset

def get_student_record_from_dataset(dataset, student_id):
    for record in dataset.get("records", []):
        if str(record["student_id"]) == str(student_id):
            return record
    return None 
    
         
         


def analytics_menu():
    config = load_config()

    while True:
        print("========== Analytics Menu ==========")
        print("1. Rank Students in Dataset")
        print("2. Show Top Performer")
        print("3. Show Lowest Performer")
        print("4. Show Weak Students")
        print("5. Show Dataset Statistics")
        print("6. Show Subject Averages")
        print("7. Show Strongest Subject Overall")
        print("8. Show Weakest Subject Overall")
        print("9. Evaluate Student in Dataset")
        print("10. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            dataset = get_dataset_input()
            if dataset:
                ranked_students = rank_students(dataset, config)
                display_ranked_students(ranked_students)
        elif choice=="2":
           dataset = get_dataset_input()
           if dataset:
              topper_info=get_topper(dataset,config)
              print("---Top Peformer---")
              display_student_evaluation(topper_info)
        
                
           
        

        elif choice=="3":
           dataset = get_dataset_input()
           if dataset:
              weakest_student_info=get_lowest_performer(dataset,config)
              print("---Lowest Peformer---")
              display_student_evaluation(weakest_student_info) 
           
        elif choice=="4":
           dataset = get_dataset_input()
           if dataset:
              weak_students_info=get_weak_students(dataset,config)
              display_weak_students(weak_students_info)  
           
           
        elif choice=="5":
           dataset = get_dataset_input()
           if dataset:
              dataset_statistics=get_dataset_statistics(dataset,config)
              display_dataset_statistics(dataset_statistics)   
           
           
        elif choice=="6":
           dataset = get_dataset_input()
           if dataset:
              subject_average=get_subject_averages(dataset)
              display_subject_averages(subject_average)   
           
        elif choice=="7":
           dataset = get_dataset_input()
           if dataset:
              strongest_subject=get_strongest_subject_overall(dataset)
              display_single_subject_insight("Strongest Subject Overall", strongest_subject)
           
        
        elif choice=="8":
           dataset = get_dataset_input()
           if dataset:
              weakest_subject=get_weakest_subject_overall(dataset)
              display_single_subject_insight("Weakest Subject Overall", weakest_subject) 
           
           
        elif choice=="9":
            dataset = get_dataset_input()
            if dataset:
                student_id = input("Student ID: ").strip()
                student_record = get_student_record_from_dataset(dataset, student_id)

                if not student_record:
                    print("Student not found in this dataset.")
                else:
                    evaluated_student = evaluate_student_record(student_record, config)
                    display_student_evaluation(evaluated_student) 
        elif choice == "10":
               break
        else:
            print("Invalid option.")  


def academic_intelligence_menu():
    while True:
        show_academic_intelligence_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                student_id = int(input("Student ID: ").strip())
            except ValueError:
                print("Invalid Value. Please enter an integer.")
                continue

            result = get_student_academic_history(student_id)
            display_student_academic_history(result)

        elif choice == "2":
            try:
                student_id = int(input("Student ID: ").strip())
            except ValueError:
                print("Invalid Value. Please enter an integer.")
                continue

            result = build_student_performance_series(student_id)
            display_student_performance_series(result)

        elif choice == "3":
            try:
                student_id = int(input("Student ID: ").strip())
            except ValueError:
                print("Invalid Value. Please enter an integer.")
                continue

            result = analyze_student_trend(student_id)
            display_student_trend(result)

        elif choice == "4":
            try:
                student_id = int(input("Student ID: ").strip())
            except ValueError:
                print("Invalid Value. Please enter an integer.")
                continue

            result = analyze_student_risk(student_id)
            display_student_risk(result)

        elif choice == "5":
            try:
                student_id = int(input("Student ID: ").strip())
            except ValueError:
                print("Invalid Value. Please enter an integer.")
                continue

            result = predict_student_performance(student_id)
            display_student_prediction(result)

        elif choice == "6":
            try:
                student_id = int(input("Student ID: ").strip())
            except ValueError:
                print("Invalid Value. Please enter an integer.")
                continue

            result = generate_student_insights(student_id)
            display_student_insights(result)

        elif choice == "7":
            break

        else:
            print("Invalid choice")





def run_cli():
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            dataset_menu()
        elif choice == "3":
            view_menu()
        elif choice == "4":
           analytics_menu()
        elif choice == "5":
           academic_intelligence_menu()
           
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")   


    
    
    