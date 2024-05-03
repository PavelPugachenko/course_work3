import json

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
        if "from" in operation:
            formatted_operation["from"] = operation["from"]
            # Другие действия для операций со значением "from"
        else:
            # Действия для остальных операций
            pass
        operations.append(formatted_operation)
    return operations
