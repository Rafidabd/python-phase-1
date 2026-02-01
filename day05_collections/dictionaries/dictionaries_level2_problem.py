
######1-Frequency counter:

n = int(input("Please enter the number of elements: "))
numbers = list(map(int, input("Please enter the numbers: ").split()))

frequency={}

for x in numbers:
    if x not in frequency:
        frequency[x]=1
    else:
    
        frequency[x]=frequency[x]+1


for key,value in frequency.items():
    print(key,value)




##Character frequency:

char = list( input("Please enter the your character: "))

frequency={}


for x in char:
     if x not in frequency:
        frequency[x]=1
     else:
    
        frequency[x]=frequency[x]+1


for key,value in frequency.items():
    print(key,value)


#3-word frequency:


sent = list( input("Please enter the your sentence: ").split())
frequency={}
for x in sent:
     if x not in frequency:
        frequency[x]=1
     else:
    
        frequency[x]=frequency[x]+1


for key,value in frequency.items():
    print(key,value)








    
        





     










   







    
