user_input = int(input("Enter a number: "))

for num in range(1,user_input+1):
	for n in range(1,6):
		print(num*n,end=" ")
	print()