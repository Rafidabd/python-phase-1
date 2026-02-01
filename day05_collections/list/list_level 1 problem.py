########Print List:
n=int(input("please enter the number of elements"))
nums=map(int,input("please enter the numbers").split())
numbers=list(nums)

for x in numbers:
    print(x)


###Sum of elements:

n=int(input("please enter the number of elements"))
nums=map(int,input("please enter the numbers").split())
numbers=list(nums)
s=0
x=1

while x<=n:
    s=s+numbers[x-1]
    x=x+1

print(s)





####count even and odd:

n=int(input("please enter the number of elements"))
nums=map(int,input("please enter the numbers").split())
numbers=list(nums)
odd=0
even=0
for x in numbers:
    if x%2!=0:
        odd=odd+1
    else:
        even=even+1

print(even,odd)




####Maximum and Minimum:

n=int(input("please enter the number of elements"))
nums=map(int,input("please enter the numbers").split())
numbers=list(nums)


maxi=numbers[0]
mini=numbers[0]

i=1

while i<n:
    if numbers[i]>maxi:
        maxi=numbers[i]
    i=i+1



while i<n:
    if numbers[i]<mini:
        mini=numbers[i]
    i=i+1

print(maxi,mini)




###Reverse a list:

n=int(input("please enter the number of elements"))
nums=map(int,input("please enter the numbers").split())
numbers=list(nums)

rev_numbers=[]

i=n-1

while i>=0:
    x=numbers[i]
    rev_numbers.append(x)

    i=i-1
print(rev_numbers)




















    


    






 





    






