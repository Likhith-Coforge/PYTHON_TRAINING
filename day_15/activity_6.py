codes_list = input("Enter list of codes: ").split(" ")

for code in codes_list:
	if code.isdigit() and code == len(code)*"0":
		break
	elif code.isdigit():
		print(code)
	elif code.isalnum():
		continue
	
