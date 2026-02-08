"""
Generate a report like:
report = {
    "total_students": 3,
    "average_math": 84.3,
    "average_cs": 91.0,
    "average_english": 85.6,
    "active_students": 2,
    "inactive_students": 1
}


"""

import json

with open("day10_JSON_handling/Data/students.json","r") as f:
    json_reader=json.load(f)

Cs={}
Math={}
English={}

for data in json_reader:
    Cs[data['name']]=data['scores']['cs']
    Math[data['name']]=data['scores']['math']
    English[data['name']]=data['scores']['english']
#Average Cs:
sum_cs=0
for x in Cs.values():
    sum_cs=sum_cs+int(x)
avg_cs=sum_cs/len(Cs)

#Average Math:
sum_math=0
for x in Math.values():
    sum_math=sum_math+int(x)
avg_math=sum_math/len(Math)
#Average English:
sum_english=0
for x in English.values():
    sum_english=sum_english+int(x)
avg_english=sum_english/len(English)


#Total student:
total_student=len(json_reader)

#active,inactive students:
active_students=0
inactive_students=0
for data in json_reader:
    if data['active']:
        active_students=active_students+1
    else:
        inactive_students=inactive_students+1

General_report={


 "total_students": total_student,
    "average_math": avg_math,
    "average_cs": avg_cs,
    "average_english": avg_english,
    "active_students": active_students,
    "inactive_students": inactive_students

}

with open("day10_JSON_handling/Data/students_report.json","w") as f:
    json.dump(General_report,f,indent=4)




