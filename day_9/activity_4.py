# Declaring a dictionary with student names and their grades
student_grades = {'Anita':92,'Ravi':85,'Kiran':76,'Zoya':88}

# Asking the user to enter the student name
std_name = input("Enter the student name: ").capitalize()

# Displaying the grade of the student, 'Student not found' if entered student # is not present 
print(student_grades.get(std_name,'Student not found'))