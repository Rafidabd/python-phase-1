from modules.storage import load_data
from modules.config_loader import load_config
config=load_config() 


def total_mark_calculator(marks_dict, subjects):
    total = 0
    for subject in subjects:
        total += marks_dict[subject]
    return total


def average_mark_calculator(total, subjects):
    return round(total / len(subjects), 2)  



def pass_fail_determiner(marks_dict,pass_mark):
   for subject_marks in marks_dict.values():
      if subject_marks<pass_mark:
         return "FAIL" 
   return "PASS"
   


def grade_calculator(average,grading_config,result):
   if result=="FAIL":
      return "F"
   stu_grade=None 
   for grade,grade_range in grading_config.items():
      if grade_range["min"]<=average<=grade_range["max"]:
         stu_grade=grade
         return stu_grade 
      
   if stu_grade==None:
      return "INVALID_GRADE_CONFIG"  
   

   
   
   


def rank_students():
    data = load_data()
    config=load_config()
    subjects=config["subjects"]
    unsorted_list=[]
    
    

    for student_id,student in data.items():
       stu_info={
          "sid":student_id,
          "name":student["name"],
          "total": total_mark_calculator(student["marks"],subjects)

       }
       unsorted_list.append(stu_info)
    sorted_students = sorted(unsorted_list, key=lambda x: x["total"], reverse=True)
    final_rank = []
    for rank, stu_dict in enumerate(sorted_students, start=1):
        sid = stu_dict["sid"]
        name = stu_dict["name"]
        total = stu_dict["total"]
        rank_info={
           "rank":rank,
           "id":sid,
           "name":name,
           "total":total
        }
        final_rank.append(rank_info)
        
        

    return final_rank


    
     
def class_average():
    data=load_data()
    config=load_config()
    subjects=config["subjects"]
    if not data:
       return {"status":"no students available"}
    total_average_sum=0
    total_student=0
    for student in data.values():
       marks_dict=student["marks"]
       total=total_mark_calculator(marks_dict,subjects)
       average=average_mark_calculator(total,subjects)
       total_average_sum=total_average_sum+average
       total_student=total_student+1
    class_average=round(total_average_sum/total_student,1)
    average_dict={
       "class_average": class_average,
       "student_count":total_student
       

    }
    return average_dict
   


def subject_topper(subject):
   
   data=load_data()
   config=load_config()
   subjects=config["subjects"]
   if subject not in subjects:
      return {"status":"invalid subject"}
   if data=={}:
      return {"status":"No students added."}
   
   max_mark=-1
   
   topper_list=[]
   for student in data.values():
      if student["marks"][subject]>max_mark:
         max_mark=student["marks"][subject]
   for student_id,student in data.items():
      if student["marks"][subject]==max_mark:
         topper_id=student_id
         topper_name=student["name"]
         topper_info={
            "id":topper_id,
            "name":topper_name,
             }
         
         topper_list.append(topper_info)
   topper_dict={ "subject":subject,
                   "highest_mark":max_mark,
                   "toppers":topper_list }

   return  topper_dict 
      


def overall_topper():
   
   rank=rank_students()
   if rank==[]:
      return {"status":"student not available"}

   topper_info_list=[]
   
   for student in rank:
      if student["rank"]==1:
         highest_total=student["total"]
         name=student["name"]
         sid=student["id"]
         topper_info={ "id":sid,
                      "name":name,
                      "total":highest_total,
                      


         }
         topper_info_list.append(topper_info)
   topper_dict={ 
      "highest_total":highest_total,
      "toppers": topper_info_list
   }
   return topper_dict 





def section_average(section):
    data = load_data()
    config = load_config()
    subjects = config["subjects"]

    if section not in config["sections"]:
        return {"status": "invalid section"}

    section_students = [
        student for student in data.values()
        if student["section"] == section
    ]

    if not section_students:
        return {"status": "no students in this section"}

    total_sum = 0

    for student in section_students:
        total = total_mark_calculator(student["marks"], subjects)
        avg = average_mark_calculator(total, subjects)
        total_sum = total_sum+avg

    final_average = round(total_sum / len(section_students), 2)

    return {
        "section": section,
        "section_average": final_average,
        "student_count": len(section_students)
    }



def section_topper(section):
    data = load_data()
    config = load_config()
    subjects = config["subjects"]

    if section not in config["sections"]:
        return {"status": "invalid section"}

    section_students = {
        sid: stu for sid, stu in data.items()
        if stu["section"] == section
    }

    if not section_students:
        return {"status": "no students in this section"}

    max_total = -1
    topper_list = []

    for sid, student in section_students.items():
        total = total_mark_calculator(student["marks"], subjects)

        if total > max_total:
            max_total = total

    for sid, student in section_students.items():
        total = total_mark_calculator(student["marks"], subjects)
        if total == max_total:
            topper_list.append({
                "id": sid,
                "name": student["name"],
                "total": total
            })

    return {
        "section": section,
        "highest_total": max_total,
        "toppers": topper_list
    }



def top_n_students(n):
    ranked_stu= rank_students()

    if not ranked_stu:
        return {"status": "no students available"}

    return ranked_stu[:n]


def filter_by_section(section):
    data = load_data()

    filtered_stu = [
        {"id": sid, "name": stu["name"], "section": stu["section"]}
        for sid, stu in data.items()
        if stu["section"] == section
    ]

    if not filtered_stu:
        return {"status": "no students in this section"}

    return filtered_stu 



def filter_by_result(result_type):
    """
    result_type should be "PASS" or "FAIL"
    """

    data = load_data()
    config = load_config()

    subjects = config["subjects"]
    pass_mark = config["marks_policy"]["pass_mark"] 

    if result_type not in ["PASS", "FAIL"]:
        return {"status": "invalid result type"}

    filtered_students = []

    for sid, student in data.items():
        marks_dict = student["marks"]

        
        result = pass_fail_determiner(marks_dict, pass_mark)

        if result == result_type:
            filtered_students.append({
                "id": sid,
                "name": student["name"],
                "section": student["section"],
                "result": result
            })

    if not filtered_students:
        return {"status": f"no students with result {result_type}"}

    return filtered_students     
 




   
   
   
         
      
      

   


    
   
   
      

      

 




        
    





    


    