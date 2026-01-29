# #1-String Compression:

# x=input("please enter your word:")
# compressed=""
# i=1
# count=1
# while i<len(x):
#     if x[i]==x[i-1]:
#         count=count+1
#     else:
#         compressed=compressed+x[i-1]+str(count)
#         count=1
#     i=i+1
# compressed=compressed+x[-1]+str(count)
# print(compressed)





# # #2-Substring counter:

# a=input("please enter your word:")
# sub=input("please enter your sub string:")
# n=len(sub)
# count=0

# i=0
# while i<=len(a)-n:
#     if a[i:(i+n)]==sub:
#         count=count+1
         
    



#     i=i+1
# print(count)





# #3-Longest common prefix:


# a,b,c=(input("please enter three words:").split())
# a1=len(a)
# b1=len(b)
# c1=len(c)



# if a1<=b1 and a1<=c1:
#     mini=a1
# elif b1<=c1 and b1<=a1:
#     mini=b1
# elif a1==b1==c1:
#     mini=a1
# elif c1<=a1 and c1<=b1:
#     mini=c1

# i=0
# pref=""

# while i<mini:
#     if a[i]==b[i]==c[i]:
#         pref=pref+a[i]
#     else:
#         break



#     i=i+1
# print(pref)




# #4-Rotation check:

# a=input("please enter first word:")
# b=input("please enter second word:") 
# c=a+a

# if len(a)==len(b):
#     is_rotation=False
#     n=len(b)
#     i=0
#     while i<=len(c)-n:
#         if b == c[i:i+n]:
#             is_rotation=True
#             break
        





#         i=i+1








# else:
    
#     print("not rotation.length number doesnt match")

# if is_rotation:
#     print("rotation")
# else:
#     print("not rotation")



#5-Replacing words:



rep={"good":"bad","Rafid":"Masfi","Boy":"Girl"}
x=input("please enter your sentence:")
x1=""
z=x.split()

for y in z:
    if y in rep.keys():
        x1=x1+rep[y]+" "
    else:
        x1=x1+y+" "
x1=x1.rstrip()

print(x1)























