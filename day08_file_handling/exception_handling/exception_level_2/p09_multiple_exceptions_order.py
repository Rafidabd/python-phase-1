f=input("please enter file name")
n=input("please enter the value")

try:
    with open(f,"a") as file:
        z=10/n
        file.write(z)
except FileNotFoundError:
    print("file doesnt exist")
except ValueError:
    print("invalid value of n")
except ZeroDivisionError:
    print("zero cant be divided")



        