def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input("please enter your number:"))
print(factorial(n))