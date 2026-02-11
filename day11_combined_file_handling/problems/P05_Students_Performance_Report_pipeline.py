# id,name,math,cs,average,grade
# 1,Rafid,85,90,87.5,A
# 2,Ayan,92,88,90,A+
# 3,Sara,70,95,82.5,B
# 4,Lina,60,65,62.5,C  
# [
#   {"id": "1", "math": 85, "cs": 90},
#   {"id": "2", "math": 92, "cs": 88},
#   {"id": "3", "math": 70, "cs": 95},
#   {"id": "4", "math": 60, "cs": 65}
# ]

import csv
import json
students_id = {}

with open("day11_combined_file_handling/data/students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students_id[row["id"]] = row["name"]
#{'1': 'Rafid', '2': 'Ayan', '3': 'Sara', '4': 'Lina'}

#Math and Cs score:
Math={}
Cs={}

with open("day11_combined_file_handling/data/scores.json", "r") as f:
    student_scores=json.load(f)
    for data in student_scores:
        Math[data["id"]]=data["math"]
        Cs[data["id"]]=data["cs"]

#{'1': 85, '2': 92, '3': 70, '4': 60} ,{'1': 90, '2': 88, '3': 95, '4': 65}

#Average:
Average = {}

for id in Math:
    avg = (Math[id] + Cs[id]) / 2
    Average[id] = avg

#Grading:
Grade={}

for id in Average:
    if Average[id]>=90:
        Grade[id]="pass"
    else:
        Grade[id]="fail"


with open("day11_combined_file_handling/data/students_pipeline.csv", "w") as writer:
    field_names=["id","name","math","cs","average","grade"]
    csv_writer=csv.DictWriter(writer,fieldnames=field_names,delimiter="\t")
    csv_writer.writeheader()
    all_reports = []

    for id in students_id:
     final_report = {
        "id": id,
        "name": students_id[id],
        "math": Math[id],
        "cs": Cs[id],
        "average": Average[id],
        "grade": Grade[id]
    }
     csv_writer.writerow(final_report)   



