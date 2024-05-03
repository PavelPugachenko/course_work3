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


data = get_data()
filtered_data = filter_data(data)
print(format_date("2019-08-26T10:50:58.294041"))
#print(last_five_operations(filtered_data))