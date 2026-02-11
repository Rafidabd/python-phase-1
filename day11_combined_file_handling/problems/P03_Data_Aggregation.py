import json
with open("day11_combined_file_handling/data/students.json","r") as json_file:
    json_reader=json.load(json_file)

Cs={}
Math={}

for data in json_reader:
    Cs[data["name"]]=data["cs"]
    Math[data["name"]]=data["math"]
Cs_total=0
Math_total=0
for values in Cs.values():
    Cs_total=Cs_total+int(values)
for values in Math.values():
    Math_total=Math_total+int(values)

Cs_Average=Cs_total/len(Cs)
Math_Average=Math_total/len(Cs)

Report={"Cs Average":Cs_Average,"Math average":Math_Average}


with open("day11_combined_file_handling/data/report.txt","w") as writer:
    writer.write(str(Report))
