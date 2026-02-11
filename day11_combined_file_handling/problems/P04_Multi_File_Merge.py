import json
import csv

students_id = {}

with open("day11_combined_file_handling/data/students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students_id[row["id"]] = row["name"]

with open("day11_combined_file_handling/data/scores.json", "r") as f:
    scores_data = json.load(f)

students_report = []

for sid, student in scores_data.items():
    name = students_id.get(sid, "Unknown")
    math_score = student["math"]
    cs_score = student["cs"]

    students_report.append({
        "id": sid,
        "name": name,
        "Math": math_score,
        "Cs": cs_score
    })

with open("day11_combined_file_handling/data/students_report.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "Math", "Cs"])
    writer.writeheader()
    writer.writerows(students_report)

print("Report generated.")




    
       
       




       




