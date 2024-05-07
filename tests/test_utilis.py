from src.utilis import get_data, filter_data, last_five_operations, format_date, format_card, get_data_format

def test_get_data():
    data = get_data()
    assert type(data) is list
    assert len(data) > 0
