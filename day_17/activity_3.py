username, firstname, lastname = input("Enter your username, firstname, lastname: ").split(" ")

password = input("Enter your password: ")

while True:
	user_name_check = password != username
	first_name_check = password != firstname
	last_name_check = password != lastname
	length_check = len(password) == 10
	has_alpha = any(char.isalpha() for char in password)
	has_digit = any(char.isdigit() for char in password)
	is_al_num = has_alpha and has_digit
	has_upper = any(ord(char)>=65 and ord(char)<=90 for char in password)
	has_lower = any(ord(char)>=97 and ord(char)<=122 for char in password)
	is_lo_up = has_upper and has_lower

	if (user_name_check and first_name_check and last_name_check and length_check and is_al_num and is_lo_up):
		break
	password = input("Enter your password: ")
