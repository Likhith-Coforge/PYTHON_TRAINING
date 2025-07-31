# Binary Search 

nums_list = [1,2,3,4,5,6,7,8,9,10]

key = int(input("Enter the element that need to be searched: "))

low = 0
high = len(nums_list) - 1

while low<=high:
	mid = (low+high)//2
	if nums_list[mid] == key:
		print(f"{key} found at position {mid} in the list")
		break
	elif key < nums_list[mid]:
		high = mid - 1
	elif key > nums_list[mid]:
		low = low + 1
else:
	print(f"{key} not found")