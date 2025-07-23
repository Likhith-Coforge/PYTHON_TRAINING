access_data={
(103,209):"Alice",
(104,210):"Bob",
(105,211):"Charlie",
(106,212):"Diana"
}

"""
# Solution-1
access_data_list = list(access_data.items())

access_data_list[0] = access_data_list[0][::-1]
access_data_list[1] = access_data_list[1][::-1]
access_data_list[2] = access_data_list[2][::-1]
access_data_list[3] = access_data_list[3][::-1]

access_data = dict(access_data_list)

user_input = input("Enter the student name: ").capitalize()

print(access_data.get(user_input,"Not found"))
"""

# Solution-2
access_data = dict(zip(access_data.values(),access_data.keys()))

user_input = input("Enter the student name: ").capitalize()

print(access_data.get(user_input,"Not found"))


