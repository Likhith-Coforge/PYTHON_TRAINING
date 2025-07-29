bool_1,bool_2,bool_3 = input("Enter three booleans(True/False): ").split(" ")

bool_dict = {'True':1,'False':0}

true_check = bool_dict[bool_1] + bool_dict[bool_2] + bool_dict[bool_3]

result = (true_check == 1) and "Exactly one" or "Nope"

if result:
	print(result)

