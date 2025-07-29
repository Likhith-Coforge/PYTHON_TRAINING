user_num = int(input("Enter a integer: "))

binary_val_user_num = bin(user_num)

if binary_val_user_num[-1] == '1':
	print("Odd")
else:
	print("Even")