num1, num2 = map(int,input("Enter two integers: ").split(" "))

odd_num_check = ((bin(num1)[-1] == '1') and (bin(num2)[-1] != '1') or (bin(num1)[-1] != '1') and (bin(num2)[-1] == '1'))

if odd_num_check:
	print("Exactly one is odd!")