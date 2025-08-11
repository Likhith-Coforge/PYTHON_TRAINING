import csv

with open("data.csv",newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		if not any(cell.strip() for cell in row):
			continue
		print(row)