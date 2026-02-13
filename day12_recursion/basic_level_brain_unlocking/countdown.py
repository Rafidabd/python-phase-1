#build a function that prints numbers from 1 to n,using recursion:

def countdown(n):
    if n==0:
        return 
    countdown(n-1)
    print(n)

n=int(input("please enter your number:"))
countdown(n)
