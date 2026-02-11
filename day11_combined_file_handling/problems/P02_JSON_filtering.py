import json

with open("day11_combined_file_handling/data/students.json","r") as json_file:
   json_reader=json.load(json_file)


for data in json_reader:
   if int(data["math"])>=90:
      print(data["name"],data["math"])