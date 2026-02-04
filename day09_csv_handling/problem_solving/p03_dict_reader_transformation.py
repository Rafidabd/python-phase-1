import csv
with open("day09_csv_handling/data_files/marks.csv","r") as reader:
    csv_reader=csv.DictReader(reader) 
    with open("day09_csv_handling/data_files/status_students.csv","w") as writer:
        field_names=["name","roll","marks","status"]
        csv_writer=csv.DictWriter(writer,fieldnames=field_names,delimiter="\t")
        csv_writer.writeheader
        for line in csv_reader:
            line["name"]=line["name"].upper()
            if int(line["marks"])>=50:
                
                line["status"]="pass"
            else:
                
                line["status"]="fail"
            csv_writer.writerow(line)
