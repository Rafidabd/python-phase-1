"""
student.py

Contains all student management operations.

This module handles core CRUD functionality:
adding students, viewing student records,
editing student details, and deleting students.

It also validates input data using the rules
defined in the configuration file.
"""
from modules.storage import load_data,save_data 
from modules.config_loader import load_config
from modules.analytics import total_mark_calculator,average_mark_calculator,grade_calculator,pass_fail_determiner




def add_student(sid, name, section, mark_dict):
    """
    Adds a new student to the system.

    The function checks several things before adding:
    - student ID must be unique.
    - section must exist in config.
    - subjects must match the configured subjects 
    - marks must be within the allowed range.range is checked.

    If everything is valid, the student record
    is saved to the JSON database.

    Args to be provided:
        sid (str): student ID
        name (str): student name
        section (str): section name
        mark_dict (dict): dictionary of subject marks.

    Returns:
        dict: status message indicating success or error 
    """
    
    config=load_config()
    
    
    existing_data=load_data()
    if not sid or not name or not section:
            return {"status":"error.empty field"}  
    
    

    if sid in existing_data:
        return{"status":"error.id exists"} 
    
    
    if section not in config["sections"]:
        return {"status":"error.invalid section"} 
    for marks in mark_dict.values():
         if marks is None:
               return {"status":"error.Blank in mark input"}  
              

    for subject in mark_dict.keys():
         if subject not in config["subjects"]:
              return {"status":"error.invalid subject"} 
    if not set(mark_dict.keys()) == set(config["subjects"]):
         return {"status":"error.wrong number of subjects"} 
         
         
    
         
    

    min_mark=int(config["marks_policy"]["min_mark"])
    max_mark=int(config["marks_policy"]["max_mark"])
    
    
    for mark in mark_dict.values():
            
            if not min_mark<=mark<=max_mark:
                 return {"status":"error.invalid mark"}  
    added_data={"name":name,
                     "section":section,
                     "marks":mark_dict}
                
    existing_data[sid]=added_data
    save_data(existing_data) 
    return {"status":"success"}  
    
       
        
            
    
        
        
        
def view_student(student_id):
    """
    Retrieves a full report of a student.

    The report includes:
    - basic information
    - subject marks
    - total marks
    - average marks
    - pass/fail result
    - grade

    If the student ID does not exist,
    an error message is returned rather than crashing..

    Args to be provided:
        student_id (str): ID of the student 

    Returns:
        dict: detailed student report 
    """
    data=load_data()
    config=load_config()
    if student_id not in data:
         return {"status":"Student not found"}
    student = data[student_id]

    name = student["name"]
    section = student["section"]
    marks_dict = student["marks"]
    subjects=config["subjects"]
    pass_mark=config["marks_policy"]["pass_mark"]
    grading_config=config["grading_system"]
    total=total_mark_calculator(marks_dict,subjects)
    average=average_mark_calculator(total,subjects)
    result=pass_fail_determiner(marks_dict,pass_mark)
    grade=grade_calculator(average,grading_config,result) 
    if grade=="INVALID_GRADE_CONFIG":
         return {"status":"Error.invalid grade config"}  

    stu_status={ "id":student_id,
                "name":name,
                "section":section,
                "marks":marks_dict,
                "total":total,
                "average":average,
                "result":result,
                "grade":grade

         




    }
    return stu_status   


def edit_student(sid,name,section,mark_dict):
     """
    Updates the information of an existing student.

    The function performs the same validations
    as add_student to ensure the updated data
    follows the system rules.

    Args provided:
        sid (str): student ID
        name (str): updated name
        section (str): updated section
        mark_dict (dict): updated marks 

    Returns:
        dict: status message indicating success or error.
    """
     data=load_data()
     config=load_config()
     if not sid or not name or not section:
            return {"status":"error.empty field"}  
     if sid not in data:
          return {"status": "error.student not found"}
     if section not in config["sections"]:
        return {"status":"error.invalid section"} 
     for marks in mark_dict.values():
         if marks==None:
               return {"status":"error.Blank in mark input"}  
              

     for subject in mark_dict.keys():
         if subject not in config["subjects"]:
              return {"status":"error.invalid subject"} 
     if not set(mark_dict.keys()) == set(config["subjects"]):
         return {"status":"error.wrong number of subjects"}
     min_mark=int(config["marks_policy"]["min_mark"])
     max_mark=int(config["marks_policy"]["max_mark"])
    
    
     for mark in mark_dict.values():
            mark=int(mark)
            if not min_mark<=mark<=max_mark:
                 return {"status":"error.invalid mark"}  
     edited_data={"name":name,
                     "section":section,
                     "marks":mark_dict}
                
     data[sid]=edited_data 
     save_data(data)
     return {"status":"success"}   

def delete_student(sid):
    """
    Removes a student from the database.

    If the given student ID exists, the record
    is deleted and the updated data is saved.
    Otherwise an error message is returned.

    Args provided:
        sid (str): student ID

    Returns:
        dict: status message .
    """
    data = load_data()

    if sid not in data:
        return {"status": "error.student not found"}

    del data[sid]
    save_data(data)

    return {"status": "success"}    
 
     
     
     
     





    





