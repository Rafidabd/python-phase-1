# #1-marks grader:

# Marks={"rahim":85,"Karim":95,"Ahmed":80}
# j=len(Marks)
# total=0

# for x in Marks.values():
#     total=(total+x)

# avg=total/j
# maxi=Marks["rahim"]

# for x in Marks.values():
#     if x>maxi:
#         maxi=x
    

# for key,values in Marks.items():
#     if values==maxi:
#         top=key

# print("topper is",top ,"and average value is",avg)




#2-reverse dictionary:


Marks={"rahim":85,"Karim":95,"Ahmed":80}

reversed_dict={}

for x,y in Marks.items():

    reversed_dict[y]=x

print(reversed_dict)

   



#3-merging two dictionaries:


Marks_1={"rahim":85,"Karim":95,"Ahmed":80}
Marks_2={"rahim":85,"musa":99,"nayan":80}

merg_dict={}

for x,y in Marks_2.items():
    if x not in Marks_1.keys():
        Marks_1.update({x:y})


print(Marks_1)



 


   
















    



