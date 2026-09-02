import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

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
        if record.get("device") != device:
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

def allocate_record_to_plan(device, record_date, amount):
    headers, row = get_device_plan(device)

    if row is None:
        return [], convert_amount(amount)

    completed_amounts = get_completed_amounts(device)

    remaining_amount = convert_amount(amount)
    allocations = []

    for column_index in range(1, len(headers)):
        header = str(headers[column_index]).strip()

        if header.lower() != "skola":
            continue

        planned_debt = convert_amount(
            row[column_index]
        )

        completed_debt = completed_amounts["Skola"]

        unpaid_debt = max(
            planned_debt - completed_debt,
            0
        )

        amount_for_debt = min(
            remaining_amount,
            unpaid_debt
        )

        if amount_for_debt > 0:
            allocations.append({
                "target": "Skola",
                "amount": amount_for_debt
            })

            remaining_amount -= amount_for_debt

        break

    if remaining_amount == 0:
        return allocations, 0

    record_date_object = datetime.strptime(
        record_date,
        "%Y-%m-%d"
    ).date()

    date_columns = []

    for column_index in range(1, len(headers)):
        header = str(headers[column_index]).strip()

        if header.lower() == "skola":
            continue

        try:
            deadline_date = datetime.strptime(
                header,
                "%Y-%m-%d"
            ).date()
        except ValueError:
            continue

        if deadline_date >= record_date_object:
            date_columns.append(
                (
                    deadline_date,
                    column_index,
                    header
                )
            )

    date_columns.sort(
        key=lambda column: column[0]
    )

    for deadline_date, column_index, deadline_text in date_columns:
        planned_amount = convert_amount(
            row[column_index]
        )

        if planned_amount == 0:
            continue

        completed_amount = completed_amounts[
            deadline_text
        ]

        available_amount = max(
            planned_amount - completed_amount,
            0
        )

        amount_for_deadline = min(
            remaining_amount,
            available_amount
        )

        if amount_for_deadline > 0:
            allocations.append({
                "target": deadline_text,
                "amount": amount_for_deadline
            })

            remaining_amount -= amount_for_deadline

        if remaining_amount == 0:
            break

    return allocations, remaining_amount