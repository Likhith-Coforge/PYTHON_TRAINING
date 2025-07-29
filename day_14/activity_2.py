user_name, user_password = input("Enter your username and password: ").split(" ")

grant_access = (user_name == 'admin') and (user_password=='secret123' or user_password == 'letmein')

if grant_access:
	print('Access Granted!')