user_pwd = input("Enter your password: ")

special_chars = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','|','\\',':',';','"',"'",'<','>',',','.','?','/']

len_check = len(user_pwd) == 8
has_upper = any(ord(char)>=65 and ord(char)<=90 for char in user_pwd)
has_lower = any(ord(char)>=97 and ord(char)<=122 for char in user_pwd)
has_digit = any(char.isdigit() for char in user_pwd)
has_special_char = any(char if char in special_chars else 0 for char in user_pwd)

has_all_cases = (len_check and has_upper and has_lower and has_digit and has_special_char)

has_case1_case2 = len_check and has_upper

has_case3_case4 = has_lower and has_digit

if has_all_cases:
	print("Strong")
elif has_case3_case4:
	print("Moderate")
elif has_case1_case2:
	print("Weak")
else:
	print("Invalid Password")