 #####Prime checker:

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


 n=int(input("please enter any number"))
 j=func_prime(n)

 print(j)




############# sum of prime numbers:


def sum_prime(x):
    if x < 2:
        return 0

    z = 0

    for i in range(2, x + 1):
        is_prime = True

        for k in range(2, i):
            if i % k == 0:
                is_prime = False
                break

        if is_prime:
            z += i

    return z


n = int(input("please enter any number: "))
result = sum_prime(n)
print(result)




        


    

            
    
        
        
        

    
