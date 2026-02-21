from modules.student import add_student,view_student
from modules.analytics import rank_students,class_average,subject_topper
from modules.export import export_leaderboard,student_report



def menu():
    print("\n1.Add student")
    print("2.View Student")
    print("3.Show Ranking")
    print("4.Show Subject Topper")
    print("5.Show Class Average")
   
    print("6.Export Student Report")
    print("7.Export Leaderboard")
    print("8.Exit")
   
    

    action=int(input("please enter your option:"))

    if action==1:
        sid=input("ID:")
        name=input("Name:")
        section=input("Section:")
        Physics=input("Physics Mark:")
        Math=input("Math Mark:")
        English=input("English Mark:")
        add_student(sid,name,section,Physics,Math,English)
        print("Student's infos have been added succesfully")
    elif action==2:
        sid=input("ID:")
        info=view_student(sid)
        print(info)

    elif action==3:
        ranking=rank_students()
        for rank, sid, name, total in ranking:
           print(f"{rank}. {name} (ID: {sid}) → {total}")

    elif action==4:
        subject=input("Please enter your subject:").title()
        topper=subject_topper(subject)
        print(f"Top scorer in {subject}: {topper['name']} with {topper['marks'][subject]}")


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
        
    

        





