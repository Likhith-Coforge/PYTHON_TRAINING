num_list = list(map(int,input("Enter the numbers: ").split(" ")))

def freq_count(nums_list):

	freq_count_num = {}

	for num in nums_list:
		if num not in freq_count_num:
			freq_count_num[num] = nums_list.count(num)
	
	return list(freq_count_num.items())

print(freq_count(num_list))