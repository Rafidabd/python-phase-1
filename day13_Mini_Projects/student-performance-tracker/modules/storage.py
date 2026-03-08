"""
storage.py

Handles all file-based data storage operations.

This module is responsible for loading and saving
student data from the JSON database file. It ensures
that the required folders and files exist before
performing any read or write operations.
"""
import json
from pathlib import Path 
from modules.config_loader import load_config

# Loading the path from config
DATA_FILE = Path(load_config()["data_file"])

def load_data():
    """
    Loads student data from the JSON database we have.

    If the data folder or the JSON file does not exist,
    the function creates them first so the program
    does not crash.safety ensured first

    If the file is empty or corrupted, an empty
    dictionary is returned instead rather than crashing.

    Returns:
        dict: dictionary containing all student records.
    """

    # First,Ensure parent folder exists (data/)
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    # If file doesn't exist, create empty JSON file
    if not DATA_FILE.exists():
        DATA_FILE.write_text("{}", encoding="utf-8")

    # then,Load and return JSON
    try:
     with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    except json.JSONDecodeError:
      return {} 

def save_data(data):
    """
    Saves student data to the JSON file.

    This function overwrites the existing file
    with the updated data provided. It also ensures that
    the data folder exists before writing.safety ensured

    Args:
        data (dict): dictionary containing all
        student information to be saved 
    """

    # Ensure folder exists before saving
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)   