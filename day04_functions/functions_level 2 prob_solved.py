###Maximum number:

def max_func(x,y):
    if x>y:
        return x
    elif x==y:
        return "equal"
    else:
        return y
    

n1,n2=map(int,input("please enter two numbers").split())
z= max_func(n1,n2)
print(z)



####digit counter:

def dig_count(x):
    count=0
    while x>0:

        if x%10>0:
            count=count+1
        x=x//10
    return count


n=int(input("please enter any number"))
dig=dig_count(n)
print(dig)




#####Factorial func:

def func_fact(x):
    fact=1
    while x>=1:
        fact=fact*x
        x=x-1
    return fact
    
    

     

n=int(input("please enter any number"))
z=func_fact(n)
print(z)











     

    
