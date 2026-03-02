from modules.student import add_student,view_student
from modules.analytics import rank_students,class_average,subject_topper,overall_topper
from modules.export import export_leaderboard,student_report
from modules.config_loader import load_config



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
        if "status" in average:
            print(average["status"])
        else: 
            print("========== CLASS AVERAGE ==========")
            student_count=average["student_count"]
            class_average_number=average["class_average"]
            print()
            print(f"Total Students: {student_count}")
            print(f"Class Average : {class_average_number}")
            print()
    

        
        


        
    elif action==6:
        toppers=overall_topper()
        if "status" in toppers:
            print(toppers["status"])
        else:
            highest_total=toppers["highest_total"]

            print("==========Overall Topper==========")
            print(f"Highest Total: {highest_total}")
            if len(toppers["toppers"])>1:
                print("Toppers:")
            else:
                print("Topper:")
            print(f"{'ID':>8} {'Name':<18} {'Total':>8} ")
            print("-------------------------------------------------------")
            for student in toppers["toppers"]:
                sid=student["id"]
                name=student["name"]
                total=student["total"]
                print(f"{sid:>8} {name:<18} {total:>8} ")
            print() 



        

        

    elif action==7:
        student_id=input("Please enter your ID:")
        report=view_student(student_id)
        if "status" in report:
            print(report["status"])
        else:
            sid=report["id"]
            name=report["name"]
            section=report["section"]
            marks_dict=report["marks"]
            total=report["total"]
            average=report["average"]
            result=report["result"]
            grade=report["grade"]
            print("========== STUDENT REPORT ==========")
            print()
            print(f"{'ID':<10}:{sid}")
            print(f"{'Name':<10 }:{name}")
            print(f"{'Section':<10 }:{section}")
            print()
            print("Marks:")
            print("------------------------------------------")
            print(f"{'Subject':<20} {'Mark':>8}")
            print("------------------------------------------")
            for subject,mark in marks_dict.items():
                print(f"{subject:<20} {mark:>8}")
            print("------------------------------------------")
            print(f"{'Total':<10}: {total}")
            print(f"{'Average':<10}: {average}")
            print(f"{'Result':<10}: {result}")
            print(f"{'Grade':<10}: {grade}")

            print() 



        
    elif action==8:
        exit()
    else:
        print("invalid option")    
        
    

        





