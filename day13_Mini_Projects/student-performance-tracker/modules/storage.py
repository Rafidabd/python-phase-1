import json
from pathlib import Path
from modules.config_loader import load_config

# Loading the path from config
DATA_FILE = Path(load_config()["data_file"])

def load_data():
    """
    Load student data from JSON file.
    Ensures folder and file exist.
    Returning the dict,
    """

    # First,Ensure parent folder exists (data/)
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    # If file doesn't exist, create empty JSON file
    if not DATA_FILE.exists():
        DATA_FILE.write_text("{}", encoding="utf-8")

    # then,Load and return JSON
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    """
    Save student data to JSON file.
    """

    # Ensure folder exists before saving
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4) 