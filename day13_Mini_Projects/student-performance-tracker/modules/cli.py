from modules.student import add_student,view_student,edit_student,delete_student
from modules.analytics import rank_students,class_average,subject_topper,overall_topper,section_average,section_topper,top_n_students,filter_by_result,filter_by_section
from modules.export import export_leaderboard,student_report
from modules.config_loader import load_config
from modules.display import display_ranking,display_class_average,display_overall_topper,display_student_report,display_subj_topper
from modules.display import display_section_toppers,display_section_average,display_filtered_section,display_filtered_by_result


def menu():
    print("\n1.Add student")
    print("2.View Student")
    print("3.Show Ranking")
    print("4.Show Subject Topper")
    print("5.Show Class Average")
   
    print("6.Show Overall Toppers")
    print("7.Full Student Report")
    print("8.Edit Student")
    print("9.Delete Student")
    print("10.Section Average")
    print("11.Section Topper") 
    print("12.Top n Students") 
    print("13.Filter by Section") 
    print("14.Filter by Result(PASS/FAIL)")

    config=load_config()  
    

    try:
     action = int(input("please enter your option: ").strip())
    except ValueError:
     print("Invalid option. Must be a number.")
     return 

    if action==1:
        sid=input("ID: ").strip()
        name=input("Name: ").strip()
        section=input("Section: ").strip() 
        mark_dict={}
        min_mark=config["marks_policy"]["min_mark"]
        max_mark=config["marks_policy"]["max_mark"]
        for subject in config["subjects"]:
            try:
             mark=int(input(f"{subject} mark:"))
            except ValueError:
                print("Invalid input.Must be a number")
                return 
            if mark < min_mark or mark > max_mark:
                   print("Mark out of allowed range")
                   return
            mark_dict[subject]=mark
        action_result=add_student(sid,name,section,mark_dict)
        print(action_result["status"])  


        

        
    elif action==2:
        sid=input("ID:")
        info=view_student(sid)
        if "status" in info:
            print(info["status"]) 
        else:
         print(info) 

    elif action==3:
        rank=rank_students()
        display_ranking(rank)

       
             
    elif action==4:
        subject=input("Please enter your subject: ").strip().lower()
        subj_topper=subject_topper(subject) 
        display_subj_topper(subj_topper) 

    
        
    elif action==5:
        average=class_average()
        display_class_average(average)

        
    elif action==6:
        toppers=overall_topper()
        display_overall_topper(toppers)
    
    
    elif action==7:
        student_id=input("Please enter your ID: ").strip()
        report=view_student(student_id)
        display_student_report(report)

        
    elif action==8:
        sid=input("ID: ").strip()
        name=input("Name: ").strip()
        section=input("Section: ").strip() 
        mark_dict={}
        min_mark=config["marks_policy"]["min_mark"]
        max_mark=config["marks_policy"]["max_mark"]
        for subject in config["subjects"]:
            try:
             mark=int(input(f"{subject} mark:"))
            except ValueError:
                print("Invalid input.Must be a number")
                return 
            if mark < min_mark or mark > max_mark:
                   print("Mark out of allowed range")
                   return
            mark_dict[subject]=mark
        action_result=edit_student(sid,name,section,mark_dict)
        print(action_result["status"])   

       
        
    elif action==9:
        confirmation=input("Are you sure?(y/n)").lower()
        if confirmation=="y":
            sid = input("Enter ID to delete: ").strip()
            result = delete_student(sid)
            print(result["status"])
        elif confirmation=="n":
            return 
        else:
            print("Choose correct option.")
            return 
    
    elif action==10:
        section=input("Please enter your section: ").strip().upper()
        average=section_average(section)
        display_section_average(section)
       
    
    elif action==11:
        section=input("Please enter your section: ").strip().upper()
        topper=section_topper(section)
        display_section_toppers(topper) 
    

    elif action==12:
        try:
            n=int(input("Please enter the value of N: "))
        except ValueError:
            print("Invalid input.Please enter an integer")
            return
        n_rank=top_n_students(n)
        display_ranking(n) 
    
    elif action==13:
        try:
         section=str(input("Please enter your section: ").strip().upper())
         
        except ValueError:
            print("Invalid Input")
            return
        filtered_section=filter_by_section(section) 
        display_filtered_section(section) 
    
    
    
    
    elif action == 14:
   
     result_type = input("Enter PASS or FAIL: ").strip().upper()
     result = filter_by_result(result_type)
     display_filtered_by_result(result) 

        

    

    



    
    
    

       
    else:

        print("invalid option")        
    
        
    

        





