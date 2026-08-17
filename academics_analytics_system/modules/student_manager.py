"""
Handles student identity operations:
- add student
- update student
- delete student
- get student
""" 

from modules.storage import load_json, save_json
from pathlib import Path
from modules.config_loader import load_config
from utils.helpers import (
    validate_board,
    validate_student_id_uniqueness,
    is_valid_int,
    is_valid_str,
    student_finder_by_id,
    class_roll_uniqueness,
    normalize_name,
)

BASE_DIR = Path(__file__).resolve().parent.parent
students_file_path = BASE_DIR / "data" / "students.json" 


def get_all_students():
    loaded_students = load_json(students_file_path)
    return loaded_students["students"]


def get_student_by_id(student_id):
    students = get_all_students()
    student_info = student_finder_by_id(students, student_id)
    return student_info


def add_student(
    student_id,
    name,
    institution,
    section,
    board,
    batch,
    class_roll,
    board_roll=None,
    board_registration=None,
   ):
    config = load_config()
    boards = config["boards"]

    students_data = load_json(students_file_path)
    students = students_data["students"]

    # Basic field validation
    name_validation = is_valid_str(name)
    institution_validation = is_valid_str(institution)
    section_validation = is_valid_str(section)
    student_id_validation = is_valid_int(student_id)
    batch_validation = is_valid_int(batch)
    class_roll_validation = is_valid_int(class_roll)

    if name_validation["status"] == "error":
        return name_validation
    if institution_validation["status"] == "error":
        return institution_validation
    if section_validation["status"] == "error":
        return section_validation
    if student_id_validation["status"] == "error":
        return student_id_validation
    if batch_validation["status"] == "error":
        return batch_validation
    if class_roll_validation["status"] == "error":
        return class_roll_validation

    # Optional integer fields
    if board_roll not in (None, ""):
        board_roll_validation = is_valid_int(board_roll)
        if board_roll_validation["status"] == "error":
            return board_roll_validation
    else:
        board_roll = None

    if board_registration not in (None, ""):
        board_registration_validation = is_valid_int(board_registration)
        if board_registration_validation["status"] == "error":
            return board_registration_validation
    else:
        board_registration = None

    # Business rule validations:-
    board_validation = validate_board(board, boards)
    if board_validation["status"] == "error":
        return board_validation

    student_id_uniqueness = validate_student_id_uniqueness(students, student_id)
    if student_id_uniqueness["status"] == "error":
        return student_id_uniqueness

    class_roll_unique = class_roll_uniqueness(
        students, institution, section, batch, class_roll
    )
    if class_roll_unique["status"] == "error":
        return class_roll_unique

    # Normalize values
    normalized_name = normalize_name(name)
    normalized_institution = institution.strip()
    normalized_section = section.strip()
    normalized_board = board.strip()

    # Build student object
    student_dict = {
        "id": student_id,
        "name": normalized_name,
        "institution": normalized_institution,
        "section": normalized_section,
        "board": normalized_board,
        "batch": batch,
        "class_roll": class_roll,
        "board_roll": board_roll,
        "board_registration": board_registration,
    }

    students.append(student_dict)
    save_json(students_file_path, students_data)

    return {
        "status": "success",
        "message": "Student added successfully."
    } 


def update_student(student_id,name,institution,section,board,batch,class_roll,board_roll=None,board_registration=None):
    config=load_config()
    boards=config["boards"]

    students_data=load_json(students_file_path)
    students=students_data["students"]

    target_student=student_finder_by_id(students,student_id)
    if target_student is None:
        return {"status":"error","message":"Student not found."}

    name_validation=is_valid_str(name,"Name")
    institution_validation=is_valid_str(institution,"Institution")
    section_validation=is_valid_str(section,"Section")
    batch_validation=is_valid_int(batch,"Batch")
    class_roll_validation=is_valid_int(class_roll,"Class roll")
    board_validation=validate_board(board,boards)

    if name_validation["status"]=="error":
        return name_validation
    if institution_validation["status"]=="error":
        return institution_validation
    if section_validation["status"]=="error":
        return section_validation
    if batch_validation["status"]=="error":
        return batch_validation
    if class_roll_validation["status"]=="error":
        return class_roll_validation
    if board_validation["status"]=="error":
        return board_validation

    if board_roll not in (None,""):
        board_roll_validation=is_valid_int(board_roll,"Board roll")
        if board_roll_validation["status"]=="error":
            return board_roll_validation
    else:
        board_roll=None

    if board_registration not in (None,""):
        board_registration_validation=is_valid_int(board_registration,"Board registration")
        if board_registration_validation["status"]=="error":
            return board_registration_validation
    else:
        board_registration=None

    class_roll_check=class_roll_uniqueness(
        students,
        institution,
        section,
        batch,
        class_roll,
        exclude_student_id=student_id
    )
    if class_roll_check["status"]=="error":
        return class_roll_check

    for student in students:
        if student["id"]==student_id:
            student["name"]=normalize_name(name)
            student["institution"]=institution.strip()
            student["section"]=section.strip()
            student["board"]=board.strip()
            student["batch"]=batch
            student["class_roll"]=class_roll
            student["board_roll"]=board_roll
            student["board_registration"]=board_registration
            break

    save_json(students_file_path,students_data)
    return {"status":"success","message":"Student updated successfully."}


def delete_student(student_id):
    students_data=load_json(students_file_path)
    students=students_data["students"]

    target_student=student_finder_by_id(students,student_id)
    if target_student is None:
        return {"status":"error","message":"Student not found."}

    datasets_data=load_json("data/datasets.json")
    datasets=datasets_data["datasets"]

    for dataset in datasets:
        for record in dataset["records"]:
            if record["student_id"]==student_id:
                return {"status":"error","message":"Cannot delete student with linked academic records."}

    updated_students=[]
    for student in students:
        if student["id"]!=student_id:
            updated_students.append(student)

    students_data["students"]=updated_students
    save_json(students_file_path,students_data)
    return {"status":"success","message":"Student deleted successfully."} 


     
def get_student_record_from_dataset(dataset, student_id):
    for record in dataset.get("records", []):
        if str(record["student_id"]) == str(student_id):
            return record

    return None      
     
     
     





