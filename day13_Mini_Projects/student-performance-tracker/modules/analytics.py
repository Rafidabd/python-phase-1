from modules.storage import load_data
from modules.config_loader import load_config
config=load_config()


def total_mark_calculator(marks_dict, subjects):
    total = 0
    for subject in subjects:
        total += marks_dict[subject]
    return total


def average_mark_calculator(total, subjects):
    return round(total / len(subjects), 1) 



def pass_fail_determiner(marks_dict,pass_mark):
   for subject_marks in marks_dict.values():
      if subject_marks<pass_mark:
         return "FAIL" 
   return "PASS"
   


def grade_calculator(average,grading_config,result):
   if result=="FAIL":
      return "F"
   stu_grade=None 
   for grade,range in grading_config.items():
      if range["min"]<=average<=range["max"]:
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
    if data=={}:
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

   
   
   
         
      
      

   


    
   
   
      

      

 




        
    





    


    