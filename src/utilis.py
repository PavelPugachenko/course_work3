import json
from datetime import datetime

def get_data():
    """Чтение данных"""
    with open("../data/operations.json", encoding="utf-8") as f:
        return json.load(f)

def filter_data(data):
    """Операции с значением ключа state executed"""
    filter_operations = [operation for operation in data if operation.get("state") and operation["state"] == "EXECUTED"]
    return filter_operations

def last_five_operations(data):
    """Сортировка и вывод последних 5 операций"""
    sorted_operations = sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted_operations[:5]


def format_date(date: str):
    """Возвращает строку даты в формате гггг-мм-дд"""
    date_format = date.split("T")[0]
    year, month, day = date_format.split("-")
    return f"{day}.{month}.{year}"

def format_card(card: str):
    "скрытие счетов"
    card = card.split()
    card_number = card.pop()
    card_name = " ".join(card)
    if card_name.lower() == "счет":
        number_secret = "**" + card_number[-4:]
    else:
        number_secret = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_name} {number_secret}"

def get_data_format(data):
    operations = []
    for operation in data:
        formatted_operation = {}
        formatted_operation["date"] = format_date(operation["date"])
        formatted_operation["description"] = operation["description"]
        formatted_operation["amount"] = operation["operationAmount"]["amount"]
        formatted_operation["name"] = operation["operationAmount"]["currency"]["name"]
        if "from" in operation:
            formatted_operation["from"] = format_card(operation["from"])
        else:
            formatted_operation["from"] = ""
        if "to" in operation:
            formatted_operation["to"] = format_card(operation["to"])
        else:
            formatted_operation["to"] = ""

        operations.append(formatted_operation)
    return operations

def print_res(data):
    new_format = []

    for obj in data:
        new_str = f"{obj['date']} {obj['description']}\n"
        if obj['from']:
            new_str += f"{obj['from']} -> {obj['to']}\n"
        else:
            new_str += f"{obj['to']}\n"
        new_str += f"{obj['amount']} {obj['name']}"
        new_format.append(new_str)

    for line in new_format:
        print(line)
        print("\n")
