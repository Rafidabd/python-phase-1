"""
export.py

Handles exporting analytical data to external files.

Currently this module exports the class leaderboard
into a CSV file so it can be opened using spreadsheet
software such as Excel or Google Sheets.
"""
from modules.analytics import rank_students
from pathlib import Path
import csv 


def export_leaderboard():
    """
    Exports the class leaderboard to a CSV file.

    The function generates the student ranking
    and saves it inside the Reports folder as
    'leaderboard.csv'.

    The file includes:
    - rank
    - student ID
    - student name
    - total marks

    Returns:
        dict: status message and file path
    """
    ranking = rank_students()

    
    if not ranking:
        return {"status":"no students available"}

    
    reports_folder = Path("Reports")
    reports_folder.mkdir(parents=True,  exist_ok=True)

    file_path = reports_folder /  "leaderboard.csv"

    with open(file_path, "w", newline="", encoding= "utf-8") as file:
        field_names = ["rank", "id", "name", "total"]

        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        for student in ranking:
            writer.writerow(student)

    return {
        "status": "success",
        "file": str(file_path) 
    }  
 

            


    



    




        
