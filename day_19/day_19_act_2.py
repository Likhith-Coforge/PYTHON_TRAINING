from random import choice

participants = ["Michael","Jim","Pam","Dwight","Angela"]

for name in participants:
	index = participants.index(name)
	pair_list = participants[index+1:]+participants[:index]
	secret_santa_pair_name = choice(pair_list)
	print(f"{name} -> {secret_santa_pair_name}")