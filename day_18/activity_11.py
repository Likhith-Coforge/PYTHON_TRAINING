user_input = input("Enter a string: ").lower()

result = {char for char in user_input if char in ['a','e','i','o','u']}

print(result)