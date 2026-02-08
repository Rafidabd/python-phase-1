import json

with open("day10_JSON_handling/Data/students.json","r") as f:
    json_reader=json.load(f)
    for data in json_reader:
        data['age']=int(data['age'])+5
    with open("day10_JSON_handling/Data/output.json","w") as file:
        json.dump(json_reader,file,indent=4)
    
    

    

