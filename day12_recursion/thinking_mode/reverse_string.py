def reverse(x):
    n=len(x)
    if len(x)==1:
        return x
    return x[n-1]+reverse(x[0:n-1])

x=input("please enter your word:")
print(reverse(x))


    
    