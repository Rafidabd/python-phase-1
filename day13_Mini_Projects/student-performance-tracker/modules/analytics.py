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
   for grade,range in grading_config:
      if range["min"]<=average<=range["max"]:
         stu_grade=grade
   if stu_grade==None:
      return "INVALID_GRADE_CONFIG" 

   
   
   


# def rank_students():
#     data = load_data()
#     rank_unsorted = []

#     for student_id in data:
#         total = total_mark(student_id)
#         name = data[student_id]["name"]
#         rank_unsorted.append((student_id, name, total))

#     # sort by total marks (highest first)
#     sorted_students = sorted(rank_unsorted, key=lambda x: x[2], reverse=True)

#     final_rank = []
#     for rank, stu_tuple in enumerate(sorted_students, start=1):
#         sid = stu_tuple[0]
#         name = stu_tuple[1]
#         total = stu_tuple[2]
#         final_rank.append((rank, sid, name, total))

#     return final_rank


# def class_average():
#    data=load_data()
#    whole_total=0
#    total_enlisted_student=0
#    for student_id in data:
#       whole_total=whole_total+total_mark(student_id)
      
#       total_enlisted_student=total_enlisted_student+1
    
#    whole_class_average=whole_total/total_enlisted_student
#    return whole_class_average



# def subject_topper(subject):
   
#    data=load_data()
#    first_student_id = list(data.keys())[0]
#    if subject in data[first_student_id]["marks"]:
#       top_mark=-1
#       topper_id=None

#       for student_id in data:
      
#          x=int(data[student_id]["marks"][subject])
#          if x>top_mark:
#           top_mark=x
#           topper_id=student_id
    
#       subj_topper_info=data[topper_id]

#       return subj_topper_info  
#    else:
#       return "invalid subject"
   
# def overall_topper():
#    data=load_data()
#    rank=rank_students()
#    topper_list=[]
   
#    topper_mark=rank[0][3]
#    for ranking,id,name,total in rank:
#       if total==topper_mark: 
#          joint_topper_id=id
#          topper_list.append((ranking,joint_topper_id,name,total))
#    return topper_list 
         
         
      
      

   


    
   
   
      

      

 




        
    





    


    