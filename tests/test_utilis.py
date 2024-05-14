from src.utilis import get_data, filter_data, last_five_operations, format_date, format_card, get_data_format, print_res

def test_format_date_valid():
    input_date = "2022-06-01T12:30:45"
    expected_output = "01.06.2022"
    assert format_date(input_date) == expected_output
def test_get_data_format_empty_input():
    assert get_data_format([]) == []
def test_filter_data_single_operation():
    data = [{"id": 1, "state": "EXECUTED"}]
    assert filter_data(data) == [{"id": 1, "state": "EXECUTED"}]

def test_last_five_operations(data):
    result = last_five_operations(data)
    assert len(result) == 5
    assert [x["date"] for x in result ] == ['2019-08-26T10:50:58.294041', '2019-07-12T20:41:47.882230', '2019-07-03T18:35:29.512364', '2018-12-20T16:43:26.929246', '2018-06-30T02:08:58.425572']

def test_format_card():
    card = "MasterCard 7158300734726758"
    account = "Счет 35383033474447895560"
    assert format_card(card) == "MasterCard 7158 30** **** 6758"
    assert format_card(account) == "Счет **5560"

def test_get_data_format(data):
    assert get_data_format(data) == [{'date': '26.08.2019', 'description': 'Перевод организации', 'amount': '31957.58', 'name': 'руб.', 'from': 'Maestro 1596 83** **** 5199', 'to': 'Счет **9589'}, {'date': '03.07.2019', 'description': 'Перевод организации', 'amount': '8221.37', 'name': 'USD', 'from': 'MasterCard 7158 30** **** 6758', 'to': 'Счет **5560'}, {'date': '30.06.2018', 'description': 'Перевод организации', 'amount': '9824.07', 'name': 'USD', 'from': 'Счет **6952', 'to': 'Счет **6702'}, {'date': '23.03.2018', 'description': 'Открытие вклада', 'amount': '48223.05', 'name': 'руб.', 'from': '', 'to': 'Счет **2431'}, {'date': '20.12.2018', 'description': 'Перевод организации', 'amount': '70946.18', 'name': 'USD', 'from': 'Счет **5355', 'to': 'Счет **6366'}, {'date': '12.07.2019', 'description': 'Перевод организации', 'amount': '51463.70', 'name': 'USD', 'from': 'Счет **4368', 'to': 'Счет **8358'}]

def test_print_res(data, capsys):
    data = get_data_format(data[:2])
    print_res(data)
    message = capsys.readouterr()
    assert message.out == '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n\n\n03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD\n\n\n'






