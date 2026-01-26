contacts={
"Rafid":"01748219007",
"Abdullah":"01792213099",
"Kanak": "01898761375",
"Kazim":"0178410071",
"Masfi": "0138989811"

}


while True: 




    n = int(input(
    "Please enter your option:\n"
    "1. Add contact\n"
    "2. Search contact\n"
    "3. Delete contact\n"
    "4. Exit\n"))





    if n==4:
        print("exiting programme")
        break
    elif n==1:
        name=input("please enter your name")
        number=input("please enter your number")
        contacts.update({name:number})
        print("contact added succesfully")
    elif n==2:
        name=input("please enter your name")
        if name in contacts:
            z=contacts[name]
            print("your number is",z)
        else:
            print("number not in the contact")
    elif n==3:
        name=input("please enter your name")
        
        if name in contacts:
         contacts.pop(name)
         print("contact deleted succesfully")

        else:
            print("number not in the contact")
    else:
        print("invalid input")






    


    










  



