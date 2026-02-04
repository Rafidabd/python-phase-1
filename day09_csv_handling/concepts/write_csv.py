import csv

# with open("day09_csv_handling/sample.csv","r") as file:
#     csv_reader=csv.reader(file)
#     with open("new_csv_file.csv","w") as new_file:
#         csv_writer=csv.writer(new_file,delimiter="\t")  ##By defeault delimiter will be comma,for different ones,we gotta pass in another arguement

#         for line in csv_reader:
#             csv_writer.writerow(line)


##but if we put custom delimiter,then while printing or reading the file,we need to specify it
with open("day09_csv_handling/new_csv_file.csv","r") as file:
    csv_reader=csv.reader(file,delimiter="\t")
    for line in csv_reader:
        print(line)


