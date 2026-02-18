import json  #python needs json module to read or write it
DATA_FILE = "day13_Mini_Projects/data/students.json"
BASE_STRUCTURE={

    "students":[]  
}

def load_data():
    try:
        with open (DATA_FILE,"r",encoding="utf-8") as reader:
            student_data=json.load(reader)
            return student_data
        """
         This function loads student data from our JSON file.
        Returns dictionary with key 'students'.
        """
    except FileNotFoundError:
        return BASE_STRUCTURE.copy()

def save_data(modified_data):
    with open (DATA_FILE,"w",encoding="utf-8") as writer:
        json.dump(modified_data,writer,indent=4)
    """
    this function saves student data dictionary to JSON file.
    """




    

