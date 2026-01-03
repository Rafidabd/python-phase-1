#basics : comparisons
language='abdc'

if language=='python':
  #the condition 
 print("language is python") ##the execution
elif language=='java':
   print('language is java')

else:     
   print("no match available")


##==============######

#boolean operators:
player='Bangladeshi' 
bowtype="batsman"
if player=='Bangladeshi' and bowtype=='bowler' : ## we can use 'or' or 'not'  too
 print("he is mustafizur")
else:
 print("he is not mustafiz.might be someone else")
 
 #*************************#

 ##object identity : if two objects have same id
 a=[1,2,3]
 b=[1,2,3]
 print (a==b) # this will print true
 print(id(a))
 print(id(b))
 print(a is b) #this will print false..as they are diff obj 

 #but if we write in b=a,then both of them will be true

 #false values:

 condition="false" # /0/{}/()/''

 if condition:
   print('taken as true')
 else:
   print('taken as false')  


###problem 1: numb checking

numb=int(input("please enter a number"))
if numb==0 :
 print("that is zero")
elif numb<0:
  print("negative number")
else:
  print("positive integer")

  #~~~~~~~~~~~~~~~~~~~~~~~~#

  #problem 2: even or odd
numb=int(input("please enter a number"))
if numb%2==0 :
    print("even")
else :
 print("odd") 


 ##problem 3: Grade system

numb=int(input("please enter a number"))

if numb>=80:
  
 print("A+")

elif 70<=numb<80:
  print("A")

elif 60<=numb<70:
  print("A-")
elif 40<=numb<60:
  
 print("B")

elif 0<=numb<40:
  
 print("F")

else:
 print("not a valid number")



#problem 4: simple calculator


num1,num2,operator=input("please enter two numbers and the operator").split()
num_1=int(num1) 
num_2=int(num2)
if operator=='+' :
  print(num_1+num_2)

elif operator=='-' :
  print(num_1-num_2)

elif operator=='*' :
  print(num_1*num_2)

elif operator=='/' :
  print(num_1/num_2)
else:
  print("operator not available.operation cant be done")

  






  





