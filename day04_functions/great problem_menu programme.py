def func_prime(x):
    if x<=1:
        z="not prime"
    else:
        i=2
        is_prime=True
        while i*i<=x:
            if x%i==0:
                is_prime=False
                break
            i=i+1
        if is_prime:
            z="prime"
        else:
            z="not prime"
    return z



def func_armstrong(x):
 
    
 s=0
 a=x

 while x>0:
    dig=x%10
    s=s+pow(dig,3)

    x=x//10

 if (s==a):
    p="armstrong"
 else:
   p="not armstrong"
 return p



def func_pallindrome(n):
 

 x=n
 rev=0

 while x>0:
    dig=x%10
    rev=rev*10+dig
    x=x//10

 if (rev==n):
   q="pallindrome"
 else:
    q="not pallindrome"
 return q



def func_menu(m):
   if m=="prime":
      n=int(input("please enter your number"))
      y=func_prime(n)
   elif m=="armstrong":
      n=int(input("please enter your number"))
      y=func_armstrong(n)

   elif m=="pallindrome":
      n=int(input("please enter your number"))
      y=func_pallindrome(n)
   else:
      y="Not available"

   return y



x=input("please enter your operation").strip().lower()
k=func_menu(x)
print(k)







      



