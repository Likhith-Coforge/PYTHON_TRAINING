n1 = int(input("Enter a integer: "))
n2 = int(input("Enter a integer: "))

min_num = n1<n2 and n1 or n2
max_num = n1<n2 and n2 or n1

id = 2

gcd = 1 

if max_num%min_num==0:
	gcd = min_num
else:
	while id != min_num:
		if n1%id == 0 and n2%id == 0:
			gcd = id
		id += 1

print(f"Greatest Common Divisor of {n1} and {n2} is {gcd}")