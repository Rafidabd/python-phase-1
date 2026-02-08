"""
JSON=Structured data representation
*A neutral lang for data.
# CSV = Excel sheet
  JSON = Organized file cabinet with folders inside folders
#--------------#Mapping of JSON:
JSON	        Python
Object {}	     dict
Array []	     list
String	         str
Number	       int / float
true / false   True / False
null	          None
"""
import json
# with open ("day10_JSON_handling/Data/students.json") as f:
#     data=json.load(f)    ##Now json file-------->Python
#     print(data)
#     print(type(data))
#     #Accesing the Data:
#     print(data[0]['scores']['cs'])  #First list index,then dictionaries inside.


#----------------------------------------#
#*******# Iterating JSON:
with open ("day10_JSON_handling/Data/students.json") as f:
    students_data=json.load(f)

for students in students_data:
    print(students['name'],students['skills'])





  
