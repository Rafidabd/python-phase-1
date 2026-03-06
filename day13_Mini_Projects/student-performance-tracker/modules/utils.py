from pathlib import Path

def ensure_reports_folder():
  
    reports_folder = Path("Reports")
    reports_folder.mkdir(parents=True, exist_ok=True)
    return reports_folder    