import csv
filename = "aapl.csv"  # File name
fields = []  # Column names
rows = []    # Data rows

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)  # Reader object

    fields = next(csvreader)  # Read header
    for row in csvreader:     # Read rows
        rows.append(row)

    print("Total no. of rows: %d" % csvreader.line_num)  # Row count

print('Field names are: ' + ', '.join(fields))

print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s" % col, end=" ")
    print('\n')

import csv
filename = "university_records.csv"
with open(filename, mode='r') as file:
    csv_reader = csv.DictReader(file)  # Create DictReader

    data_list = []  # List to store dictionaries
    for row in csv_reader:
        data_list.append(row)

for data in data_list:
    print(data)

