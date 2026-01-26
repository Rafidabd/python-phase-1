#1-removing duplicates:

# n=int(input("please enter number of elements"))
# numb=list(map(int,input("please enter  numbers").split()))
# sets=list(set(numb))
# print(sets)


# #2-count unique elements:
# n=int(input("please enter number of elements"))
# numb=set(map(int,input("please enter  numbers").split()))
# i=0
# for x in numb:
#     i=i+1
# print("total unique element:",i)


#3-membership check:


numbers={1,2,3,4,5,6,7}
x=int(input("please enter the element you want to search for:"))

if x in numbers:
    print("found")
else:
    print("not found")

