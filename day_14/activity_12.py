nums_list = list(map(int,input("Enter numbers: ").split(" ")))

sorted_list = sorted(nums_list)

result = (nums_list == sorted_list and "Ascending") or (nums_list == sorted_list[::-1] and "Descending")

if result:
	print(result)
else:
	print("Unordered")