"""
config_loader.py

Loads configuration settings for the application.

The configuration file contains system settings such as
subjects, grading system, section names, mark policies,
and data file locations. This module provides a simple
function to access those settings throughout the project.
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config.json"

def load_config():
    """
    this func Loads the configuration settings from config.json.

    This file contains things like:
    - list of subjects 
    -  section names
    -  grading system
    - marks policy 

    The function simply reads the JSON file and
    returns the data as a Python dictionary so
    other modules can use it.So Helpful for a config based tool.

    Returns:
        dict: configuration data from config.json
    """

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data












