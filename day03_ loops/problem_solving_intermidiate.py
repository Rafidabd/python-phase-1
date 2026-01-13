# #digit count: $$$$$$$$$$$$$$$$$$$$$$$$$

# PROBLEM: digit count

n = int(input("Please enter any number: "))

count = 0

while n > 0:
    count = count + 1
    n = n // 10

print("total digit number is", count)







####### Sum of digits:
n = int(input("Please enter any number: "))
s=0
while n>0:
    rem=n%10
    s=s+rem
    n=n//10

print("number of digits are", s)




########Reverse a number:

n = int(input("Please enter any number: "))
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10

print("reversed number:",rev)




######multiplication table:

n = int(input("Please enter any number: "))

for x in range (1,11):
    print (n, "*",x,"=" ,n*x)






#####prime number checking:

n = int(input("Please enter any number: "))
if n<=1:
    print("not prime")
else:
    i=2
    is_prime= True
    while i*i<n:
        if n%i==0:
            is_prime= False
            break
        i=i+1
    
    if is_prime:
        print("prime number")
    else:
        print("not prime")




###Sum of prime numbers from 1 to N:

# Sum of prime numbers from 1 to N

n = int(input("Please enter any number: "))

if n < 2:
    print("Sum is 0")
else:
    s = 0
    i = 2

    while i <= n:
        is_prime = True
        x = 2

        while x * x <= i:
            if i % x == 0:
                is_prime = False
                break
            x += 1

        if is_prime:
            s += i

        i += 1

    print("Sum of primes is:", s)









    ####checking perfect number:

n = int(input("Please enter any number: "))
i=2
s=1
while i<n:

    is_div=True
    rem=n%i
    if rem==0:
        is_div= True
    else:
        is_div=False
    if is_div:
        s=s+i
    i=i+1

if (s==n)  :
    print("perfect number")
else:
    print("not perfect")




##### finding GCD:


num1,num2=map(int,input("please enter the numbers").split())

if num1<num2: 
    x=num1
    y=num2
else:
    x=num2
    y=num1 
z=x
while z>1:
   
    if y%z==0 and x%z==0:
        gcd=z
        break
    z=z-1

print("your gcd is ",z)










   
  




 



       
     

          
        
        
            

        

     



      

   


    







  





