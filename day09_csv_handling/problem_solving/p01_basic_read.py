import csv
with open ("day09_csv_handling/data_files/students.csv") as reader:
    csv_reader=csv.reader(reader)
    header=next(reader)
    print("Header:",header)
    i=0
    for line in csv_reader:
        i=i+1
    

        print(line)
    print(f"total number of students:{i}")
