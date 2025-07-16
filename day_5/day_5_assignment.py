space_seperated_nums = input()

nums_list = space_seperated_nums.split(' ')

original_nums_list = nums_list[1::3]

original_nums_list.reverse()

required_string = ""

for val in original_nums_list:
    required_string+=chr(int(val))

print(required_string)
