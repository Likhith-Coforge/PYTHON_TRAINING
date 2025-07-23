student_names = set()

user_input1 = input("Enter your full_name: ")
student_names.add(user_input1)

user_input2 = input("Enter your full_name: ")

student_names.add(user_input2 not in student_names and user_input2 or input('User name already exists, please enter a valid name with unique identification: '))

user_input2 = input("Enter your full_name: ")

student_names.add(user_input2 not in student_names and user_input2 or input('User name already exists, please enter a valid name with unique identification: '))

# repeat the above process if you want to add more names into the student_names set

print(student_names)
