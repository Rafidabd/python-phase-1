"""
display.py

Contains functions responsible for printing
formatted outputs to the terminal.

These functions take processed data from the
analytics module and present it in a clean
and readable format for the user.
"""
def display_ranking(rank):
    """
    Displays the class ranking in a formatted table.

    The function receives the ranking data
    and prints it in a clean console layout
    showing rank, ID, name and total marks.

    Args:
        rank (list or dict): ranking data returned
        from the analytics module .
    """
    if "status" in rank:
            print(rank["status"])
    else:
         print("========== CLASS RANKING ==========")
         print()
         print(f"{'rank':>6} {'id':>8} {'Name':<25} {'total':>8}") 
         print("---------------------------------------------")
         for student in rank:
             stu_rank=student["rank"]
             sid=student["id"]
             name=student["name"]
             total=student["total"]
             print(f"{stu_rank:>6} {sid:>8} {name:<25} {total:>8}") 
         print() 

def display_subj_topper(subj_topper):
     
     """
    Displays the topper info in a formatted message.

    The function receives the data of a topper
    and prints it in a clean console layout
    showing ID and Name.

    Args:
        subject topper (list or dict):  data returned
        from the analytics module .
    """
    
     if "status" in subj_topper:
            print(subj_topper["status"])
     else:
            highest_mark=subj_topper["highest_mark"]
            print("========== SUBJECT TOPPER ==========")
            print(f"Subject: {subj_topper['subject']}")
            print(F"Highest Mark: {highest_mark}")
            print()
            if len(subj_topper["toppers"])>1:
                print("Toppers:")
            else:
                print("Topper:")
            print(f"{'ID':>8} {'Name':<18} ")
            print("--------------------------------------------")
            for student in subj_topper["toppers"]:
                sid=student["id"]
                name=student["name"]
                print(f"{sid:>8} {name:<18} ")
            print() 

def display_class_average(average):
     
     """
    Displays the class average in a formatted message.

    The function receives the dict of class average
    and prints it in a clean console layout
    showing class average and total student count.

    Args:
        class average (list or dict):  data returned
        from the analytics module .
    """
     if "status" in average:
            print(average["status"])
     else: 
            print("========== CLASS AVERAGE ==========")
            student_count=average["student_count"]
            class_average_number=average["class_average"]
            print()
            print(f"Total Students: {student_count}")
            print(f"Class Average : {class_average_number}")
            print()
     
def display_overall_topper(toppers):
     """
    Displays the toppers in a formatted table.

    The function receives the dict of top scorers
    and prints it in a clean console layout
    showing ID ,Name and total marks of the toppers.

    Args:
        toppers (list or dict):  data returned
        from the analytics module .
    """
     if "status" in toppers:
            print(toppers["status"])
     else:
            highest_total=toppers["highest_total"]

            print("==========Overall Topper==========")
            print(f"Highest Total: {highest_total}")
            if len(toppers["toppers"])>1:
                print("Toppers:")
            else:
                print("Topper:")
            print(f"{'ID':>8} {'Name':<25} {'Total':>8} ")
            print("-------------------------------------------------------")
            for student in toppers["toppers"]:
                sid=student["id"]
                name=student["name"]
                total=student["total"]
                print(f"{sid:>8} {name:<25} {total:>8} ") 
            print() 


def display_student_report(report):
    """
    Prints a detailed report of a student.

    The report includes personal information,
    subject marks, total marks, average,
    result and grade.

    Args:
        report (dict): student report data
    """
    if "status" in report:
            print(report["status"])
    else:
            sid=report["id"]
            name=report["name"]
            section=report["section"]
            marks_dict=report["marks"]
            total=report["total"]
            average=report["average"]
            result=report["result"]
            grade=report["grade"]
            print("========== STUDENT REPORT ==========")
            print()
            print(f"{'ID':<10}:{sid}")
            print(f"{'Name':<10}:{name}")
            print(f"{'Section':<10}:{section}")
            print()
            print("Marks:")
            print("------------------------------------------")
            print(f"{'Subject':<20} {'Mark':>8}")
            print("------------------------------------------")
            for subject,mark in marks_dict.items():
                print(f"{subject:<20} {mark:>8}")
            print("------------------------------------------")
            print(f"{'Total':<10}: {total}")
            print(f"{'Average':<10}: {average}")
            print(f"{'Result':<10}: {result}")
            print(f"{'Grade':<10}: {grade}")

            print()    

def display_section_average(average):
      """
    Displays the  average of a particular section in a formatted message.

    The function receives the dict of section average
    and prints it in a clean console layout
    showing zection average and total student count of the section.

    Args:
        section average (list or dict):  data returned
        from the analytics module .
     """
      
      
      if 'status' in average:
            print(average["status"])
      else:
           print("========== SECTION AVERAGE==========")
           print()
           section=average["section"]
           final_average=average["section_average"]
           student_count=average["student_count"]
           print(f"{'Section':<10}:{section}")
           print(f"{'Average':<10}:{final_average}")
           print(f"{'Total Students':<10}:{student_count}") 
           print()  


def display_section_toppers(toppers):
        """
    Displays the toppers of a particular section in a formatted table.

    The function receives the dict of top scorers in a section
    and prints it in a clean console layout
    showing ID ,Name and total marks of the toppers.

    Args:
        section_toppers (list or dict):  data returned
        from the analytics module .
        """
        if 'status' in toppers:
            print(toppers["status"])
        else:
             print("========== SECTION TOPPERS==========")
             print()
             section=toppers["section"]
             highest_total=toppers["highest_total"]
             if len(toppers["toppers"])>1:
              print("Toppers List")
             else:
                  print("Topper:")
             print("------------------------------------------")
             print(f"{'ID':>8} {'Name':<25} {'Total':>8} ")
             print("-------------------------------------------------------")
             for student in toppers["toppers"]:
                sid=student["id"]
                name=student["name"]
                total=student["total"]
                print(f"{sid:>8} {name:<25} {total:>8} ") 
             print()   

def display_filtered_section(section):
     """
    Displays the students of a particular section in a formatted table.

    The function receives the dict of the students of a particular section
    and prints it in a clean console layout
    showing ID ,Name and section of the students.

    Args:
        section_students_list (list):  data returned
        from the analytics module . 
     """
     if "status" in section:
          print(section["status"])
     else:
          print(f"============Section {section[0]["section"]}============") 
          print()
          print(f"{'ID':>8} {'Name':<25} {'Section':<8} ")
          for students in section:
               sid=students["id"]
               name=students["name"]
               section=students["section"]
               print(f"{sid:>8} {name:<25} {section:<8} ")
          print()



def display_filtered_by_result(data):
    """
    Displays the students filtered by results.

    The function receives the dict of the filtered students
    and prints it in a clean console layout
    showing ID ,Name , section and results of the students. 

    Args:
        filtered_students_list (list):  data returned
        from the analytics module . 
     """
    

    
    if isinstance(data, dict) and "status" in data:
        print(data["status"])
        return

    print("===== FILTERED STUDENTS =====")
    print()
    print(f"{'ID':<10} {'Name':<25} {'Section':<10} {'Result':<10}")
    print("-" * 55)

    for student in data:
        print(f"{student['id']:<10} "
              f"{student['name']:<25} "
              f"{student['section']:<10} "
              f"{student['result']:<10}")

    print("-" * 55)
    print(f"Total Students: {len(data)}\n")       



          

     

     

             

            
     
     
           
           
     



     
     

     
     

    



