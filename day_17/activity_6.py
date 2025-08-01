n1 = int(input("Enter a integer: "))
n2 = int(input("Enter a integer: "))

min_num = n1<n2 and n1 or n2
max_num = n1<n2 and n2 or n1

id = 1

while True:
	if (max_num*id)%min_num == 0:
		lcm_id = id
		break
	id += 1
print(f"Least Common Multiple of {n1} and {n2} is {lcm_id*max_num}")