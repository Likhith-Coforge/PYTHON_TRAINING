user_value = input("Enter some value: ")

cond_dict = {'False':0,'0':0}

result = cond_dict.get(user_value,1)

if result:
	print("Truthy")
else:
	print("Falsy")