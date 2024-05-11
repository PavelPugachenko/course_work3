from src.utilis import get_data, filter_data, last_five_operations, format_date, format_card, get_data_format

def test_format_date_valid():
    input_date = "2022-06-01T12:30:45"
    expected_output = "01.06.2022"
    assert format_date(input_date) == expected_output


# Тест для функции filter_data
def test_filter_data():
    data = [{"state": "EXECUTED"}, {"state": "PENDING"}, {"state": "EXECUTED"}]
    filtered_data = filter_data(data)
    assert len(filtered_data) == 2
    for operation in filtered_data:
        assert operation["state"] == "EXECUTED"

# Тест для функции last_five_operations
def test_last_five_operations():
    data = [{"date": "2022-05-15"}, {"date": "2022-05-14"}, {"date": "2022-05-13"}, {"date": "2022-05-12"}, {"date": "2022-05-11"}, {"date": "2022-05-10"}]
    last_operations = last_five_operations(data)
    assert len(last_operations) == 5
    expected_dates = ["2022-05-15", "2022-05-14", "2022-05-13", "2022-05-12", "2022-05-11"]
    for i, operation in enumerate(last_operations):
        assert operation["date"] == expected_dates[i]




