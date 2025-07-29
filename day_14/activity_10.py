string_1, string_2 = input("Enter two strings(seperated by a space): ").split(" ")

string_1 = string_1.lower()
string_2 = string_2.lower()

result = string_1 == string_2 and "Match" or "No match"

if result:
	print(result)

