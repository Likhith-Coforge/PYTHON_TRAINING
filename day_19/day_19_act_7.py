with open('day_19_act_4.py','r') as file:
	line_count = len(file.readlines())

with open('day_19_act_4.py','r') as file:
	space_count = file.readlines().count('\n')

print(line_count-space_count)