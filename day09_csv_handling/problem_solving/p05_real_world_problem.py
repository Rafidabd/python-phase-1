import csv

total = {}
count={}
average={}
status={}

with open("day09_csv_handling/data_files/students_2.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        # calculate total
        sid = row["id"]
        marks = int(row["marks"])
        total[sid] = total.get(sid, 0) + marks

    # reset file pointer
    f.seek(0)
    reader = csv.DictReader(f)  # reinitialize DictReader

    for row in reader:
        # calculate count
        sid = row["id"]
        count[sid] = count.get(sid, 0) + 1
    


for a,b in total.items():
    average[a]=total[a]/count[a]

for a,b in average.items():
    if int(average[a])>50:
        status[a]="pass"
    else:
        status[a]="fail"


with open("day09_csv_handling/data_files/students_summary.csv", "w", newline="") as writer:
    field_names = ["id", "name", "average", "total", "status"]
    csv_writer = csv.DictWriter(writer, fieldnames=field_names, delimiter="\t")
    csv_writer.writeheader()

    for sid in total.keys():  # iterate over unique student IDs
        # You need a name for the ID: pick first occurrence from CSV
        with open("day09_csv_handling/data_files/students_2.csv", "r") as f:
            reader = csv.DictReader(f)
            name = None
            for row in reader:
                if row["id"] == sid:
                    name = row["name"]
                    break  # first occurrence only

        csv_writer.writerow({
            "id": sid,
            "name": name,
            "average": average[sid],
            "total": total[sid],
            "status": status[sid]
        })

                         
                         








          
         
        










