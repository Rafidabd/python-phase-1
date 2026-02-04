import csv
with open("day09_csv_handling/marks.csv","r") as reader:
    csv_reader=csv.DictReader(reader) 
    with open("day09_csv_handling/passed_students.csv","w") as writer:
        field_names=["name","roll","marks"]
        csv_writer=csv.DictWriter(writer,fieldnames=field_names,delimiter="\t")
        csv_writer.writeheader
        for line in csv_reader:
            line["name"]=line["name"].upper()
            if int(line["marks"])>=50:
                csv_writer.writerow(line)
