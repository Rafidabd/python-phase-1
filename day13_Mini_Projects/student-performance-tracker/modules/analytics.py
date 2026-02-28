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
   whole_total=0
   total_enlisted_student=0
   for student_id in data:
      whole_total=whole_total+total_mark(student_id)
      
      total_enlisted_student=total_enlisted_student+1
    
   whole_class_average=whole_total/total_enlisted_student
   return whole_class_average



def subject_topper(subject):
   
   data=load_data()
   first_student_id = list(data.keys())[0]
   if subject in data[first_student_id]["marks"]:
      top_mark=-1
      topper_id=None

      for student_id in data:
      
         x=int(data[student_id]["marks"][subject])
         if x>top_mark:
          top_mark=x
          topper_id=student_id
    
      subj_topper_info=data[topper_id]

      return subj_topper_info  
   else:
      return "invalid subject"
   
def overall_topper():
   data=load_data()
   rank=rank_students()
   topper_list=[]
   
   topper_mark=rank[0][3]
   for ranking,id,name,total in rank:
      if total==topper_mark: 
         joint_topper_id=id
         topper_list.append((ranking,joint_topper_id,name,total))
   return topper_list 
         
         
      
      

   


    
   
   
      

      

 




        
    





    


    