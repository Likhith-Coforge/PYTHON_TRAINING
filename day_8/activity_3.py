students = {
"Anita":{"Math":95,"Science":89},
"Ravi":{"Math":80,"Science":92},
"Pavi":{"Math":88,"Science":85}
}

std_name = input("Enter the student name: ").capitalize()
sub_name = input("Enter the subject name: ").capitalize()

"""
if students.get(std_name,"Invalid input") == "Invalid input":
	print("Invalid Student Name")
elif students.get(sub_name,"Invalid input") == "Invalid input":
	print("Invalid Subject Name")
else:

	result = students.get(std_name).get(sub_name)
	print(f'The score for {std_name} in {sub_name} is {result}')
"""

print(students.get(std_name,{}).get(sub_name,"Invalid input"))