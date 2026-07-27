import json
from pathlib import Path

PLAN_FILE = Path("data/plan.json")

def save_plan(headers, rows):
    data = {
        "headers" : headers,
        "rows": rows
    }

    PLAN_FILE.parent.mkdir(exist_ok=True)

    with open(PLAN_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_plan():
    if not PLAN_FILE.exists():
        return

    with open(PLAN_FILE, "r", encoding="utf-8") as file:
        return json.load(file)