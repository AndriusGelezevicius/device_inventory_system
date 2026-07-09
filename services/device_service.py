import json


def load_devices():
    with open("data/devices.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["devices"]