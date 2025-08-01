n = int(input("Enter an integer: "))

def is_armstrong(num):
	org_num = num
	sum_num = 0
	num_count = 0
	while num>0:
		num_count += 1
		num //= 10
	num = org_num
	while num>0:
		sum_num += (num%10)**num_count
		num //= 10
	return org_num == sum_num

print(is_armstrong(n))
	
