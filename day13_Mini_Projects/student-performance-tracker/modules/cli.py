from modules.student import add_student,view_student
from modules.analytics import rank_students,class_average,subject_topper
from modules.export import export_leaderboard,student_report
from modules.config_loader import load_config



def menu():
    print("\n1.Add student")
    print("2.View Student")
    print("3.Show Ranking")
    print("4.Show Subject Topper")
    print("5.Show Class Average")
   
    print("6.Export Student Report")
    print("7.Export Leaderboard")
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
        if "status" in rank:
            print(rank["status"])
        else:
         print("========== CLASS RANKING ==========")
         print()
         print(f"{'rank':>6} {'id':>8} {'Name':<15} {'total':>8}")
         print("---------------------------------------------")
         for student in rank:
             stu_rank=student["rank"]
             sid=student["id"]
             name=student["name"]
             total=student["total"]
             print(f"{stu_rank:>6} {sid:>8} {name:<15} {total:>8}")
         print()
             
         

        

    elif action==4:
        subject=input("Please enter your subject: ")
        subj_topper=subject_topper(subject)
        if "status" in subj_topper:
            print(subj_topper["status"])
        else:
            highest_mark=subj_topper["highest_mark"]
            print("========== SUBJECT TOPPER ==========")
            print(f"Subject: {subj_topper['subject']}")
            print(F"Highest Mark: {highest_mark}")
            print()
            if len(subj_topper["toppers"])>1:
                print("Toppers:")
            else:
                print("Topper:")
            print(f"{'ID':>8} {'Name':<18} ")
            print("--------------------------------------------")
            for student in subj_topper["toppers"]:
                sid=student["id"]
                name=student["name"]
                print(f"{sid:>8} {name:<18} ")
            print() 

                
            
            


    elif action==5:
        average=class_average()
        print(f"Class average is {average}")
    elif action==6:
        id=input("please enter your id:")
        student_report(id)
        print("student's report has been generated")

    elif action==7:
        export_leaderboard()
        print("leaderboard has been generated")
    elif action==8:
        exit()
    else:
        print("invalid option")    
        
    

        





