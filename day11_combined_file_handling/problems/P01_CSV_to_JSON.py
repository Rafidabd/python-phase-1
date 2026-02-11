import csv
import json

with open("day11_combined_file_handling/data/students.csv") as f:
    csv_reader=csv.DictReader(f)
    list=list(csv_reader)
    with open("day11_combined_file_handling/data/students.json","w") as writer:
     json.dump(list,writer,indent=4)



