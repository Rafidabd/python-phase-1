def sum_list(x):
    
    n=len(x)
    if len(x)<=1:
        return int(x[0])
    return int(x[n-1])+sum_list(x[0:n-1])


x=input("please enter your numbers:").split()
y=list(x)
print(sum_list(y))

