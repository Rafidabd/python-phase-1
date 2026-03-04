from modules.analytics import rank_students,pass_fail_determiner,section_average,grade_calculator,average_mark_calculator,total_mark_calculator
from modules.storage import load_data,save_data
import matplotlib.pyplot as plt
from modules.config_loader import load_config
from pathlib import Path

def visualize_top_students():
    rank=rank_students()
    top_5_stu=rank[:5]
    if not top_5_stu:
        return {"status":"Student not available"}
    names=[]
    totals=[] 
    for student in top_5_stu:
        name=student["name"]
        total=student["total"]
        names.append(name)
        totals.append(total)
    plt.bar(names,totals)
    plt.title("Top Performing Students")
    plt.xlabel("Student Name")
    plt.ylabel("Total Mark")
    
    plt.xticks(rotation=45) 
    plt.tight_layout() 
 

    
    reports_folder = Path("Reports")
    reports_folder.mkdir(parents=True, exist_ok=True)

    file_path = reports_folder / "top5_students.png"

   
    plt.savefig(file_path)

    
    plt.show()

    
    plt.clf()

    return {
        "status": "success",
        "file": str(file_path)
    } 



def visualize_pass_fail_chart():
    data=load_data()
    config=load_config()
    passed_students=0
    failed_students=0
    pass_mark=config["marks_policy"]["pass_mark"]


    if not data:
        return {"status":"ERROR.No students available"}
    

    for student in data.values():
        marks_dict=student["marks"]
        result=pass_fail_determiner(marks_dict,pass_mark)
        if result=="PASS":
            passed_students=passed_students+1
        else:
            failed_students=failed_students+1
    
    Status=["PASS","FAIL"]
    Number=[passed_students,failed_students] 
    plt.bar(Status,Number)
    plt.title("Result Analysis(PASS/FAIL)")
    plt.xlabel("Result")
    plt.ylabel("Number of Students")
    
    plt.xticks(rotation=45) 
    plt.tight_layout() 
    

    
    reports_folder = Path("Reports")
    reports_folder.mkdir(parents=True, exist_ok=True)

    file_path = reports_folder / "Pass_Fail_Analysis.png" 

   
    plt.savefig(file_path)

    
    plt.show()

    
    plt.clf()

    return {
        "status": "success",
        "file": str(file_path)
    }  





def visualize_section_comparison():
    data=load_data()
    config=load_config()
    sections=config["sections"]
    if not data:
        return {"status":"Error.No student available"}
    section_names = []
    section_averages = []

    for section in sections:
      avg = section_average(section)
      if "status" in avg: 
          return {"status": avg["status"]} 
      avg_value = avg["section_average"]
      section_names.append(section)
      section_averages.append(avg_value)
    plt.bar(section_names,section_averages)
    plt.title("Section Wise Performance Analysis")
    plt.xlabel("Sections")
    plt.ylabel(" Section Average")
    plt.tick_params(axis="both") 
    plt.xticks(rotation=45) 
    plt.tight_layout()  
    

    
    reports_folder = Path("Reports")
    reports_folder.mkdir(parents=True, exist_ok=True)

    file_path = reports_folder / "Section_Comparison.png" 

   
    plt.savefig(file_path)

    
    plt.show()

    
    plt.clf()

    return {
        "status": "success",
        "file": str(file_path)
    }


def visualize_grade_distribution():
    data=load_data()
    config=load_config()
    grading_config=config["grading_system"]
    subjects=config["subjects"]
    pass_mark=config["marks_policy"]["pass_mark"]
    
    if not data:
        return{"status":"Error.No students Available"}
    grade_counts = {}
    for student in data.values(): 
        marks_dict=student["marks"]
        total=total_mark_calculator(marks_dict,subjects) 
        average=average_mark_calculator(total,subjects)
        result=pass_fail_determiner(marks_dict,pass_mark)
        grade=grade_calculator(average,grading_config,result)
        if grade not in grade_counts:
          grade_counts[grade] = 0

        grade_counts[grade] += 1
    sorted_grades = sorted(grade_counts.keys())

    grade_list = sorted_grades
    students_number = [grade_counts[grade] for grade in sorted_grades]
    plt.bar(grade_list,students_number)
    plt.title("Grade Distribution")
    plt.xlabel("Grades") 
    plt.ylabel("Number of Students")
    plt.tick_params(axis="both")
    plt.xticks(rotation=45) 
    plt.tight_layout() 
   

    
    reports_folder = Path("Reports")
    reports_folder.mkdir(parents=True, exist_ok=True)

    file_path = reports_folder / "Grade_distribution.png" 

   
    plt.savefig(file_path)

    
    plt.show()

    
    plt.clf()

    return {
        "status": "success",
        "file": str(file_path) 
    }  







    
            
    




        








