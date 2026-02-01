####2nd largest number:
n=int(input("please enter the number of elements"))
nums=map(int,input("please enter the numbers").split())
numbers=list(nums)


maxi=numbers[0]


i=1

while i<n:
    if numbers[i]>maxi:
        maxi=numbers[i]
    i=i+1

numbers_2=numbers

maxi_2=numbers_2[0]
i=1

while i<(n-1):
    if numbers_2[i]>maxi_2:
        maxi_2=numbers[i]
    i=i+1


print(maxi_2)









####Remove duplicates:


n = int(input("Please enter the number of elements: "))
numbers = list(map(int, input("Please enter the numbers: ").split()))

i = 0
while i < len(numbers):
    j = i + 1
    while j < len(numbers):
        if numbers[j] == numbers[i]:
            numbers.pop(j)  # remove duplicate
        else:
            j += 1  # only move j if we didn't pop
    i += 1

print("List without duplicates:", numbers)





   










  










    










