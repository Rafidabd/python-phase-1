##Checking if element matches:

a=set(map(int,input("please enter the element of the 1st set").split()))
b=set(map(int,input("please enter the element of the 2nd set").split()))
z=a.intersection(b)

if z==set():
    print("no common element")
else:
    print("yes.there is common element")


#Subset check:
a=set(map(int,input("please enter the element of the 1st set").split()))
b=set(map(int,input("please enter the element of the 2nd set").split()))

un=a | b

if un==a and (a!=b):
    print("2nd set is the subset of 1st one")
elif un==b and (a!=b):
    print("1st set is the subset of 2nd one")
elif a==b:
    print("both are subset of each other")

else:
    print("none of them are subsets of each oother")


##Missing number;


n=int(input("please enter the value of n:"))
a=set(map(int,input("please enter the element of the 1st set").split()))

z=set()

i=1

while i<=n:
    z.add(i)

    i=i+1

x=z-a


for y in x:
    print("your missing elements are",y)


##Unique Registration system:




names=set()



while True:

    n=int(input("1.register name 2.Exit"))
    if n==1:
        x=input("please enter your name")
        if x in names:
            print("already exists")
        else:
            names.add(x)
            print("ok")
    elif n==2:
        break
    else:
        print("invalid option")


    


 










