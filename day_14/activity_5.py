input_1 = input("Enter the input_1: ")
input_2 = input("Enter the input_2: ")
input_3 = input("Enter the input_3: ")

all_unique = input_1 != input_2 and input_1 != input_3 and input_2 != input_3

all_non_empty = input_1 and input_2 and input_3

if all_unique and all_non_empty:
	print("All unique and non-empty")