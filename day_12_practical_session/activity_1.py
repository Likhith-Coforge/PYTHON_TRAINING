user_input = input("Enter your input: ")

user_input1 = '.' in user_input and "".join(user_input.split('.')) or user_input

index = '.' in user_input and user_input.index('.')

float_input = '.' in user_input and "".join(user_input.split('.')[index:])

num_result = user_input.isdigit() and (int(user_input)%2==0 and "The given number is a even number" or "The given number is a odd number")

float_result = '.' in user_input and "".join(user_input.split('.')).isdigit() and f'Length of given input is: {len(user_input)-1}\nLength of given input after decimal point is: {len(float_input)}'

palindrome_result = user_input1.lower() == user_input1.lower()[::-1] and "The given string is a palindrome" or "The given string is not a palindrome"

other_type_result = user_input in "True False None" and "Not a valid input"

print(num_result or other_type_result or float_result or palindrome_result)
