import json
from pathlib import Path  


# Loading the path 
EXPENSE_FILE = Path("data/expenses.json")

def load_expenses():
    

    # First,Ensure parent folder exists (data/)
    EXPENSE_FILE.parent.mkdir(parents=True, exist_ok=True)

    # If file doesn't exist, create empty JSON file
    if not EXPENSE_FILE.exists():
        EXPENSE_FILE.write_text("[]", encoding="utf-8")

    # then,Load and return JSON
    try:
     with open(EXPENSE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    except json.JSONDecodeError:
      return [] 

def save_expenses(expenses):
   
    # Ensure folder exists before saving
    EXPENSE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(EXPENSE_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4)    


def generate_expense_id(expenses):

    if not expenses:
        return "E001"

    last_id = expenses[-1]["id"]

    last_number = int(last_id[1:])

    new_number = last_number + 1

    return f"E{new_number:03}" 
   

   

