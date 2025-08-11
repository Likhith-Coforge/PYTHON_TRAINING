import csv

data = []

def quote_numeric(value):
	try:
		float(value)
		return f'-{value}-'
	except ValueError:
		return value

with open('data_1.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		data.append(row)

with open('output.csv',mode="w",newline="") as file:
	writer = csv.writer(file)
	for row in data:
		writer.writerow([quote_numeric(cell) for cell in row])