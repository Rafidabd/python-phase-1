import csv
scores={}   #{'01': '99', '02': '96', '03': '88', '05': '98', '07': '99', '11': '23'} 
with open("day09_csv_handling/data_files/students_scores.csv","r") as reader:
    csv_reader=csv.DictReader(reader)
    for row in csv_reader:
        scores[row["id"]]=row["score"]
    with open("day09_csv_handling/data_files/students_id.csv","r") as f1:
        csv_reader_1=csv.DictReader(f1)
        with open("day09_csv_handling/data_files/students_final_results.csv","w") as f2:
            field_names=["id","name","score"]
            csv_writer=csv.DictWriter(f2,fieldnames=field_names,delimiter="\t")
            csv_writer.writeheader()
            for row in csv_reader_1:
                result_row={ "id":row["id"],
                             "name":row["name"],
                             "score":scores.get(row["id"],"N/A")





                }
                csv_writer.writerow(result_row)

           
    
    





        

