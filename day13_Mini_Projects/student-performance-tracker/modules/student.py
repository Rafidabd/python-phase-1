from modules.storage import load_data,save_data
from modules.config_loader import load_config
from modules.analytics import total_mark_calculator,average_mark_calculator,grade_calculator,pass_fail_determiner




def add_student(sid,name,section,mark_dict):
    config=load_config()
    
    
    existing_data=load_data()
    if not sid or not name or not section:
            return {"status":"error.empty field"}  
    
    

    if sid in existing_data:
        return{"status":"error.id exists"} 
    
    
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
    added_data={"name":name,
                     "section":section,
                     "marks":mark_dict}
                
    existing_data[sid]=added_data
    save_data(existing_data) 
    return {"status":"succesful"} 
    
       
        
            
    
        
        
        
def view_student(student_id):
    data=load_data()
    config=load_config()
    if student_id not in data:
         return {"status":"Student not found"}
    name=data[student_id]["name"]
    section=data[student_id]["section"]
    marks_dict=data[student_id]["marks"]
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
     return {"status":"succesful"}  

def delete_student(sid):
    data = load_data()

    if sid not in data:
        return {"status": "error.student not found"}

    del data[sid]
    save_data(data)

    return {"status": "success"} 
 
     
     
     
     





    





