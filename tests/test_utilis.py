from src.utilis import get_data, filter_data, last_five_operations, format_date, format_card, get_data_format

def test_format_date_valid():
    input_date = "2022-06-01T12:30:45"
    expected_output = "01.06.2022"
    assert format_date(input_date) == expected_output





