#PROBLEM 1 : print from 1 to N:

n=int(input("please enter any value"))
for x in range  (0,n+1) :
    print(x)



# PROBLEM 2:  sum of first n numbers

n=int(input("please enter any value"))
s=0
x=1

while x<=n:
  
 s=s+x
 x=x+1
print(s) 



##PROBLEM 3: EVEN NUMBERS
n=int(input("please enter any value"))

for x in range (1,n+1):
 if x%2!=0:
   continue
 else:
   print(x)




##PROBLEM 4 : Countdown

n=int(input("please enter any value"))

for x in reversed(range(1,n+1)):
  print(x)




