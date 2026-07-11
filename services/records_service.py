import json

def load_records():
    try:
        with open("data/records.json", "r", encoding="utf-8") as file:
            data = json.load(file) #jdon pakeicia i python dictonerie
        return data["records"]
    except FileNotFoundError:
        return []

def save_record(record):
    records = load_records()

    records.append(record)

    data = {
        "records": records
    }

    with open("data/records.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4) #indent - kad lengvai butu skaitomas
