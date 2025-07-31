def user_sum_func(iterable):

	total_sum = 0
	for num in iterable:
		total_sum += num
	return total_sum


nums_list = [4,3,78,25]
result = user_sum_func(nums_list)

print(result)