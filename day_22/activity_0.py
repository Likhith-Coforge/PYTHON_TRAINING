import csv

with open("data.csv") as file:
	reader = csv.DictReader(file)
	amount_sum = 0
	for row in reader:
		amount_sum += float(row['Amount'])

print(f"Sum of all values in 'Amount' column: {amount_sum}")