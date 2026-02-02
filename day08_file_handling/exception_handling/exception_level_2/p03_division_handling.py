while True:
    n1=int(input("please enter first number:"))
    n2=int(input("please enter second number:"))
    
    try:
        print(n1/n2)
        break
    except ValueError:
        print("invalid value")
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("executing the code.........")


