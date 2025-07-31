# Linear Search

nums_list = [5,3,8,6,7,2]

key = int(input("Enter the element that need to be find: "))

for idx in range(len(nums_list)):
	if key == nums_list[idx]:
		print(f"{key} found at position {idx} in the list")
		break
else:
	print(f"{key} not found")
