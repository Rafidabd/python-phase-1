from modules.student import add_student,view_student
from modules.analytics import rank_students,class_average,subject_topper,overall_topper
from modules.export import export_leaderboard,student_report
from modules.config_loader import load_config
from modules.display import display_ranking,display_class_average,display_overall_topper,display_student_report,display_subj_topper



def menu():
    print("\n1.Add student")
    print("2.View Student")
    print("3.Show Ranking")
    print("4.Show Subject Topper")
    print("5.Show Class Average")
   
    print("6.Show Overall Toppers")
    print("7.Full Student Report")
    print("8.Exit")
    config=load_config()
    

    action=int(input("please enter your option:"))

    if action==1:
        sid=input("ID:")
        name=input("Name:")
        section=input("Section:")
        mark_dict={}
        for subject in config["subjects"]:
            try:
             mark=int(input(f"{subject} mark:"))
            except ValueError:
                print("Invalid input.Must be a number")
                return 
            mark_dict[subject]=mark
        action_result=add_student(sid,name,section,mark_dict)
        print(action_result)


        

        
    elif action==2:
        sid=input("ID:")
        info=view_student(sid)
        print(info)

    elif action==3:
        rank=rank_students()
        display_ranking(rank)

       
             
    elif action==4:
        subject=input("Please enter your subject: ")
        subj_topper=subject_topper(subject)
        display_subj_topper(subj_topper)

    
        
    elif action==5:
        average=class_average()
        display_class_average(average)

        
    elif action==6:
        toppers=overall_topper()
        display_overall_topper(toppers)
    
    
    elif action==7:
        student_id=input("Please enter your ID:")
        report=view_student(student_id)
        display_student_report(report)

        
    elif action==8:
        exit()
    else:
        print("invalid option")     
        
    

        





