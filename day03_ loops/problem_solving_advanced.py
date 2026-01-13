###armstrong number checking:


n=int(input("please enter any number:"))
s=0
x=n

while x>0:
    dig=x%10
    s=s+pow(dig,3)

    x=x//10

if (s==n):
    print("armstrong number")
else:
    print("not armstrong")








########Palindrome Number checking:

n=int(input("please enter any number"))

x=n
rev=0

while x>0:
    dig=x%10
    rev=rev*10+dig
    x=x//10

if (rev==n):
    print("pallindrome")
else:
    print("not pallindrome")
    





#####Password attempt:



correct_pass= 1234




count=0

while count <3:
    password=int(input("please enter your password"))
    
    if password==correct_pass:
        print("access granted")
        break
    else:
        print("wrong password.enter again")
        count=count+1
if count==3:
    print("access denied")







###Pattern Making:


row=int(input("please enter number of rows"))
sym=input("please enter the symbol")

for x in reversed(range (1,row+1)):

    while x<=row:
        print(sym,end="")
        x=x+1
    print()
    

    
    
   
        
 



     


    







