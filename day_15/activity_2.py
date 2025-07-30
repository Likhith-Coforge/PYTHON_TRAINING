user_input = input("Enter a sentence: ").lower()

replacements = user_input.maketrans({'a':'-1','e':'-1','i':'-1','o':'-1','u':'-1'})

user_input = user_input.translate(replacements)

print(user_input.count('-1'))

