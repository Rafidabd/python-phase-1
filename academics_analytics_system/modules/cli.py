from modules.display import show_main_menu,show_dataset_menu,show_student_menu,show_view_menu,show_message,display_student,display_all_students,display_dataset,display_all_datasets
from modules.student_manager import add_student,update_student,delete_student,get_all_students
from modules.dataset_manager import create_dataset,add_student_record,get_all_datasets,get_student_by_id,get_dataset_by_name
from modules.config_loader import load_config
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

            creating_dataset = create_dataset(exam_name, dataset_type, institution, board, batch)
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
            print("Exiting...")
            break
        else:
            print("Invalid choice") 


    
    
    