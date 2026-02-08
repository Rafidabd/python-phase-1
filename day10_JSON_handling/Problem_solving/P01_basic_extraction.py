"""
print out-1.All student names

2.All students who are active = true

3.All skills of each student
"""
import json

with open("day10_JSON_handling/Data/students.json","r") as f:
    json_reader=json.load(f)

for data in json_reader:
    print(data['name'])
for data in json_reader:
     if data['active']:
        print(data['name'])
for data in json_reader:
    print(data['skills'])







