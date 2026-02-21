from modules.analytics import rank_students,total_mark,average_mark
from modules.storage import load_data
import csv 

def export_leaderboard():
    ranking = rank_students()

    with open("Reports/leaderboard.csv", "w", newline="") as writer:
        field_names = ["rank", "sid", "name", "total"]
        leaderboard_writer = csv.DictWriter(writer, fieldnames=field_names)
        leaderboard_writer.writeheader()

        for rank, sid, name, total in ranking:
            stu_info = {
                "rank": rank,
                "sid": sid,
                "name": name,
                "total": total
            }
            leaderboard_writer.writerow(stu_info)

    return "Leaderboard exported"


def student_report(student_id):
    student_data = load_data()
    student_id = str(student_id)

    totalmark = total_mark(student_id)
    average = average_mark(student_id)
    name = student_data[student_id]["name"]

    overall_rank = rank_students()
    student_rank = -1

    for rank, sid, stu_name, total in overall_rank:
        if sid == student_id:
            student_rank = rank

    with open(f"Reports/report_{student_id}.txt", "w") as writer:
        writer.write(f"Student ID: {student_id}\n")
        writer.write(f"Name: {name}\n")

        # subject marks now:
        for subject, mark in student_data[student_id]["marks"].items():
            writer.write(f"{subject}: {mark}\n")

        writer.write(f"Total Mark: {totalmark}\n")
        writer.write(f"Average Mark: {average}\n")
        writer.write(f"Ranking: {student_rank}\n")

    return "Report exported" 


            


    



    




        
