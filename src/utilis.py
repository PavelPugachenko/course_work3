import json


def get_data():
    """чтение данных"""
    with open("../data/operations.json", encoding="utf-8")  as f:
        return json.load(f)


def filter_data(data):
    filter_operations = [operation for operation in data if operation.get("state") and operation["state"] == "EXECUTED"]
    return filter_operations

data = get_data()
filter_data(data)