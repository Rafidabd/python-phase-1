import json
from pathlib import Path

from modules.storage import load_json

BASE_DIR = Path(__file__).resolve().parent.parent
config_file_path = BASE_DIR / "config" / "config.json"

def load_config():
    return load_json(config_file_path) 
