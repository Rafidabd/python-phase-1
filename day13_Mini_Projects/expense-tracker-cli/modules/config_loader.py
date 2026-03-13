import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config/categories.json"

def load_config():
   
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data 