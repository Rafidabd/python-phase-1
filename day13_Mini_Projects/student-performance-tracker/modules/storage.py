import json
from pathlib import Path

DATA_FILE = Path("data/students.json")
BASE_STRUCTURE = {}

def load_data():
    """
    Load student data from JSON file.
    Returns dict.
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return BASE_STRUCTURE.copy()

def save_data(data):
    """
    Save student data to JSON file.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4) 

    

