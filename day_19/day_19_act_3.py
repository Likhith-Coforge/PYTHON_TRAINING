from datetime import datetime, date

emp_doj = ['2024-08-04','2025-02-24','2024-01-12','2022-04-20','2021-12-14']

format_string = "%Y-%m-%d"

for emp in emp_doj:

	emp_date = datetime.strptime(emp,format_string).date()

	today = date.today()

	days = (today-emp_date).days

	print(f"{days} Days Completed")

	print(f"{days//365} Years and {(days%365)//30} Months")
	
	print()