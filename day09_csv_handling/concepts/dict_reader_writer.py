import csv 
# with open("day09_csv_handling/sample.csv","r") as file:
#     csv_reader=csv.DictReader(file)
#     for line in csv_reader:
#         print(line['email'])
 #Dictionary reading is prefered because gathering and extracting the info is much easier than the normal method


with open("day09_csv_handling/sample.csv","r") as file:
    csv_reader=csv.DictReader(file)
    with open("day09_csv_handling/sample.csv","w") as writer:
        field_names=['first name','second name','email'] #must be provided in a list
        csv_writer=csv.DictWriter(writer,fieldnames=field_names,delimiter="\t")
        csv_writer.writeheader()
        csv_writer.writerow({'first name':'alif','second name':'khan','email':'alif12@gmail.com'})
        
        # for line  in csv_reader:
        #     csv_writer.writerow(line)


        