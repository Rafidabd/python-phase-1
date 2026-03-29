"""
Handles output formatting and structured terminal display.
"""

def show_main_menu():
     print("\n1.Student Management")
     print("2.Dataset Management")
     print("3.View Data")
     print("4.Exit")
     



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

     



     


          
          
    
    
     
     


          
          
     


     




