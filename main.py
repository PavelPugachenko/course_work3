from src.utilis import get_data, filter_data, last_five_operations, get_data_format, print_res

all_data = get_data()
executed_data = filter_data(all_data)
last_five = last_five_operations(executed_data)
res = get_data_format(last_five)
print_res(res)
