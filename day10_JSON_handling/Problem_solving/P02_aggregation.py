"""
TASK:
Task

1.Compute average CS score

2.Find the student with highest math score

3.Print name + score of topper

"""
import json

with open("day10_JSON_handling/Data/students.json","r") as f:
    json_reader=json.load(f)
Cs={}
Math={}

for data in json_reader:
    Cs[data['name']]=data['scores']['cs']
    Math[data['name']]=data['scores']['math']
#Average:
sum=0
for x in Cs.values():
    sum=sum+int(x)
avg=sum/len(Cs)

#Highest Math number:
max_numb=-1
for x in Math.keys():
    if Math[x]>max_numb:
        max_numb=Math[x]
        highest_scorer_math=x
    

print(f"average cs mark is {avg}")
print(f"Highest math scorer is {highest_scorer_math} and his mark is {max_numb}")





    






