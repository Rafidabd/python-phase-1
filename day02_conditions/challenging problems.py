#problem 1 : number check

n=int(input("please enter the number"))

if n>0:
   if n%2==0:
      print("positive even")
   else:
      print("positive odd")
elif n<0:
  if n%2==0:
      print("negative even")
  else:
      print("negative odd")
else:
    print("zero")


#Problem 2: Triangle Validity

a,b,c=map(int,(input("please enter the values of the sides")).split())

if (a+b)>c and (a+c)>b and (b+c)>a :
   print ("valid triangle")
else:
   print("invalid triangle ")


##problem 3: Admission

a,b,c=map(int,input(("please enter the numbers of math,physics and english(in order)")).split())
avg=(a+b+c)/3

if avg>=75:
   if (a>=80)and (b>=75) and (c>=60):
      print("eligible")
   else: 
      print("not eligible")   

    
else: 
    print("not eligible")



###problem 4: ATM withdrawal



bal,wd=map(int,input("please enter balance and withdrawal amount").split())
rem=bal-wd

if wd%100==0:
   if rem>=500 and wd<=bal:
      print("transaction succesful")
   else:
      print("unsuccesful transaction")

else:
   print("withdrawal must be multiple of 100")



##problem 5: electricity bill (tough)

a=int(input("please enter the unit"))
b=a-100
c=a-200
d=a-300

if (a>0):
   if(b<=0):
      x= a*2 
   elif(b>0) and c<=0 :
     x=(b*3+200)
   elif (c>0 and d<=0) :
     x=(c*5+100*2+100*3)

   elif(d>0):
      x=(d*7+100*2+100*3+100*5)
      

else:
   print("invalid bill")

if(x<200):
   print("your bill is 200")
else:
   print("your bill is ", x)

####problem 6: system login (toughest)


age, attempts, admin, locked = map(int, input().split())

# 1. Input validation
if age < 0 or attempts < 0 or (admin != 0 and admin != 1) or (locked != 0 and locked != 1):
    print("Invalid input")

# 2. System lock
elif locked == 1 and admin == 0:
    print("Account locked")

# 3. Age restriction
elif age < 18 and admin == 0:
    print("Access denied")

# 4. Password attempts
elif attempts > 3 and admin == 0:
    print("Account locked")

# 5. Final access
else:
    print("Access granted")

#problem 1 : number check

n=int(input("please enter the number"))

if n>0:
   if n%2==0:
      print("positive even")
   else:
      print("positive odd")
elif n<0:
  if n%2==0:
      print("negative even")
  else:
      print("negative odd")
else:
    print("zero")


#Problem 2: Triangle Validity

a,b,c=map(int,(input("please enter the values of the sides")).split())

if (a+b)>c and (a+c)>b and (b+c)>a :
   print ("valid triangle")
else:
   print("invalid triangle ")


##problem 3: Admission

a,b,c=map(int,input(("please enter the numbers of math,physics and english(in order)")).split())
avg=(a+b+c)/3

if avg>=75:
   if (a>=80)and (b>=75) and (c>=60):
      print("eligible")
   else: 
      print("not eligible")   

    
else: 
    print("not eligible")



###problem 4: ATM withdrawal



bal,wd=map(int,input("please enter balance and withdrawal amount").split())
rem=bal-wd

if wd%100==0:
   if rem>=500 and wd<=bal:
      print("transaction succesful")
   else:
      print("unsuccesful transaction")

else:
   print("withdrawal must be multiple of 100")



##problem 5: electricity bill (tough)

a=int(input("please enter the unit"))
b=a-100
c=a-200
d=a-300

if (a>0):
   if(b<=0):
      x= a*2 
   elif(b>0) and c<=0 :
     x=(b*3+200)
   elif (c>0 and d<=0) :
     x=(c*5+100*2+100*3)

   elif(d>0):
      x=(d*7+100*2+100*3+100*5)
      

else:
   print("invalid bill")

if(x<200):
   print("your bill is 200")
else:
   print("your bill is ", x)

####problem 6: system login (toughest)


age, attempts, admin, locked = map(int, input().split())

# 1. Input validation
if age < 0 or attempts < 0 or (admin != 0 and admin != 1) or (locked != 0 and locked != 1):
    print("Invalid input")

# 2. System lock
elif locked == 1 and admin == 0:
    print("Account locked")

# 3. Age restriction
elif age < 18 and admin == 0:
    print("Access denied")

# 4. Password attempts
elif attempts > 3 and admin == 0:
    print("Account locked")

# 5. Final access
else:
    print("Access granted")
