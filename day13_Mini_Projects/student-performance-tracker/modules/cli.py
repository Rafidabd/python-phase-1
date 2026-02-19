from modules.student import add_student,view_student

def menu():
    print("\n1.Add student")
    print("2.View Student")
    print("3.Exit")

    action=input("please enter your option:")

    if action==1:
        sid=input("ID:")
        name=input("Name:")
        marks=int(input("Marks:"))
        add_student(sid,name,marks)
        print("Student's infos have been added succesfully")
    elif action==2:
        sid=input("ID:")
        info=view_student(sid)
        print(info)

    elif action==3:
        exit()




