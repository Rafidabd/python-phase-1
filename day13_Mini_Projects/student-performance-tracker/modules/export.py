from modules.analytics import rank_students,total_mark,average_mark
from modules.storage import load_data
import csv 

def export_leaderboard():
    ranking=rank_students() 
    with open ("Reports/leaderboard.csv","w") as writer:
        field_names=["rank", "sid","name" , "total"]
        leaderboard_writer=csv.DictWriter(writer,fieldnames=field_names,delimiter="\t")
        leaderboard_writer.writeheader()
        for line in ranking:
            leaderboard_writer.writerow(line)

    return leaderboard_writer


def student_report(student_id):
    student_data=load_data()
    totalmark=total_mark(student_id)
    average=average_mark(student_id)
    name=student_data[student_id]["name"]
    overall_rank=rank_students()
    student_rank=-1
    for rank, sid, stu_name, total in  overall_rank:
        if sid==student_id:
            student_rank=rank
    with open(f"reports/{student_id}".txt,"w") as writer:
        writer.writeline(f"Student ID: {student_id}\n")
        writer.writeline(f"Name: {name}\n")
        writer.writeline(f"Total Mark: {totalmark}\n")
        writer.writeline(f"Average Mark: {average}\n")
        writer.writeline(f"Ranking: {student_rank}\n")
        

            


    



    




        
