from modules.storage import load_data,save_data
from modules.config_loader import load_config




def add_student(sid,name,section,mark_dict):
    config=load_config()
    
    
    existing_data=load_data()

    if sid in existing_data:
        return "error.id exists"
    
    if section not in config["sections"]:
        return "error.wrong section"

    for subject in mark_dict.keys():
         if subject not in config["subjects"]:
              return "error.invalid subject"
    if not set(mark_dict.keys()) == set(config["subjects"]):
         return "error.wrong number of subjects"
         
         
    
         
    

    min_mark=int(config["marks_policy"]["min_mark"])
    max_mark=int(config["marks_policy"]["max_mark"])
    
    
    for mark in mark_dict.values():
            mark=int(mark)
            if not min_mark<=mark<=max_mark:
                 return "error.invalid mark"
    added_data={"name":name,
                     "section":section,
                     "marks":mark_dict}
                
    existing_data[sid]=added_data
    save_data(existing_data) 
    return "succesful" 
    
       
        
            
    
        
        
        
def view_student(student_id):
    data=load_data()
    return data.get(student_id,"Student not found")  





