# # #1-swap values:
# # a,b=map(int,input("please enter your numbers:").split())
# # x=(a,b)
# # b=x[0]
# # a=x[1]

# # print(a,b)


# # #2-Maximum and minimum:

# # numbers = list(map(int, input("please enter your numbers: ").split()))

# # def maxi_mini(q):
# #     maxi = q[0]
# #     mini = q[0]

# #     i = 1
# #     while i < len(q):
# #         if q[i] > maxi:
# #             maxi = q[i]
# #         if q[i] < mini:
# #             mini = q[i]
# #         i += 1

# #     return (mini, maxi)

# # print(maxi_mini(numbers))




# # #3-positive,negative,zero counting:

# # numbers = list(map(int, input("please enter your numbers: ").split()))

# # def numb_count(q):
# #     pos=0
# #     neg=0
# #     zero=0



# #     i=0

# #     while i<len(q):
# #         if q[i]==0:
# #             zero=zero+1
# #         elif q[i]<0:
# #             neg=neg+1
# #         elif q[i]>0:
# #             pos=pos+1
# #         i=i+1
    



# #     return (pos,neg,zero)



# # print(numb_count(numbers))




# # #4-remove duplicates:

# # numbers=list(map(int,input("enter your numbers:").split()))

# # def dup(x):
    

# #     x1=[]

# #     i=0

# #     while i<len(x):
# #         if x[i] not in x1:
# #             x1.append(x[i])
        

# #         i=i+1
    

# #     return tuple (x1)

# # print(dup(numbers))




# # #5-Unpacking nested tuple:


# # name=input("please enter your name")
# # marks=list(map(int,input("please enter your numbers").split()))

# # data=(name,tuple(marks))

# # y=data[1]
# # z=data[0]

# # total=0

# # for j in y:
# #     total=total+j
# # avg=total/len(y)


# # print("Name:",z,"Average:",avg)




# #6-tuple as dictionary:



# Students={

# ("Rafid",12611052):99,
# ("Nayan",12611051):98,
# ("Opu",12611050):97

# }




# a=input("please enter the name")
# b=int(input("please enter roll number"))

# if (a,b) in Students:

#  marks=Students.get((a,b))   
#  print(marks)
# else:
#    print("doesnt exist")


#7- Value returning:





a=list(map(int,input("please enter your numbers:").split()))





def value(x):
  
  sum=0
  for y in x:
    sum=sum+y
  avg=sum/len(x)

  return sum,avg


z=value(a)

j=z[0]
k=z[1]



print("Sum:",j,"avg:",k)

 




















    


    
    
        






