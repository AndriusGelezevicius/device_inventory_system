import json
from pathlib import Path
from collections import defaultdict
from services.records_service import load_records

PLAN_FILE = Path("data/plan.json")

def convert_amount(value):
    if value in ("", None):
        return 0

    return int(float(value))
def get_completed_amounts(device):
# suskaičiuoja jau priskirtus kiekius pagal skolą ir datas.

    completed_amounts = defaultdict(int)

    records = load_records()

    for record in records: # Paimk po vieną pridavimo įrašą iš records.json.
        if records.get("device") != device:
            continue

        allications = record.get("allocations", [])

        for allocation in allications:
            target = allocation["target"]
            amount = convert_amount(allocation["amount"])

            completed_amounts[target] += amount
    return completed_amounts


def save_plan(headers, rows):
    data = {
        "headers": headers,
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

def get_device_plan(device):
    plan = load_plan()

    if plan is None:
        return None, None

    headers = plan["headers"]
    rows = plan["rows"]

    for row in rows:
        if row[0] == device:
            return headers, row

    return None, None