employees = [("Alice",28,52345.75),("Bob",35,62300.5),("Charlie",41,70000.0),("Dana",25,48750.2)]


print("%-12s" %"Name","%3s" %"Age", "%10s" %"Salary")
for emp in employees:
	print("%-12s" %emp[0],"%3d" %emp[1], "%011.2f" %emp[2])