


while True:
    n=input("please enter your numbers:").split()
    try:
        x=list(map(int,n))
        print(x)
        break
    except ValueError:
        print("please enter a valid input")
    finally:
        print("running the code....")

    


