user_string = input("Enter a string: ")

user_list = list(user_string)
user_list.reverse()

rev_string = "".join(user_list)

result = (user_string == rev_string) and "Mirror" or "Broken"

if result:
	print(result)