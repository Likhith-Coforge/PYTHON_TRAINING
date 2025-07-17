nums_list = list(map(int,input().split(' ')))  # user input

third_ele_list = nums_list[1::3][::-1] # extracting every third char from nums_list and reversing it

second_ele_list = nums_list[::2] # extracting every second char from nums_list

combined_list = (third_ele + second_ele)*2 # combining third_ele_list and second_ele_list and mutliplying it with 2

print(combined_list) # final output