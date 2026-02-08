"""
Task

Create a new list of students who scored ≥ 90 in CS.
Save them into a new JSON file
"""
import json
with open("day10_JSON_handling/Data/students.json","r") as f:
    json_reader=json.load(f)
    topper=[]
for data in json_reader:
    if int(data['scores']['cs'])>=90:
        topper.append(data)
with open("day10_JSON_handling/Data/cs_toppers.json","w") as writer:
    json.dump(topper,writer,indent=4)


        
        






