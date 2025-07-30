org_num = int(input("Enter a positive integer: "))

count = 0

for num in range(1,org_num+1):
	print((org_num-num) * " ",end="")
	print((num+count)*"*",end="")
	print((org_num-num) * " ")
	count += 1