# Solution-1

total_sum = 0

for num in range(1,101):
	if num%2==1:
		total_sum += num
print(total_sum)


# Solution-2

odd_nums_list = list(range(1,101,2))
print(sum(odd_nums_list))

