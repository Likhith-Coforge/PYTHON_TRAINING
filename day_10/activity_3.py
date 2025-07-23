students = {'Alice','Bob','Charlie'}

len1 = len(students)

new_entries = ['Charlie','Diana','Eve','Bob','Frank']

students.update(list(set(new_entries)-students))

len2 = len(students)

print(students)
print(len2-len1)