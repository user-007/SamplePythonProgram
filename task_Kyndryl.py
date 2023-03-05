from csv import reader with open('usage_data.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header  = next(csv_reader)