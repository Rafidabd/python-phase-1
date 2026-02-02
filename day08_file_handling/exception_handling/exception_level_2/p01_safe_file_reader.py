x=input("please enter your file name:")
try:
    f=open(x)
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File doesnt exist")    
except PermissionError:
    print("no permission granted to open this file")
except Exception:
    print("sorry.error detected")
finally:
    print("running the code.......")   ##will be shown always..

    



