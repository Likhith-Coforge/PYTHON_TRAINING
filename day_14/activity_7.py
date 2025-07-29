num1, num2 = map(int,input("Enter two integers: ").split(" "))

divisibility_check = (num1%num2 == 0 and num1) or (num2%num1==0 and num2)
larger_num = num1>num2 and num1 or num2
num_sum = num1 + num2

if divisibility_check:
	print(larger_num)
else:
	print(num_sum)

