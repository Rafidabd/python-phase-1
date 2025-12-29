#problem 1 : reverse without strings

a=int(input("please enter first number"))
b=int(input("please enter second number"))
a=a+b
b=a-b
a=a-b
print(a,b)
#solution-1

#problem 2: age in seconds

age=int (input("please enter your age"))
second=age*365*24*60*60
print(second)

#solution-2


# problem 3 : 3 digit integer to be taken and show the sum and mul of the digits 

a=int(input("please enter your number"))
x=int(a%10)
y=int((a-x)/10)
z=int(y%10)
p=int ((y-z)/10)
q=int(p%10)
sum=x+z+q
mul=x*z*q
print('sum is ',sum,' and mul is ',mul)

#solution-3-first try


num = int(input("Enter a 3-digit number: "))

d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10

print("Sum:", d1 + d2 + d3)
print("Product:", d1 * d2 * d3)

#solution 3- second try and better 

#=============================#
#problem 4
