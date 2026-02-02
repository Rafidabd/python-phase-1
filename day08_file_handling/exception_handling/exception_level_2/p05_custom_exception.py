n=int(input("please enter your age: "))

try:
    if n<18:
        raise Exception
    
except ValueError:
    print("invalid value")
except Exception:
    print("Not old enough")
else:
    print("access granted")


