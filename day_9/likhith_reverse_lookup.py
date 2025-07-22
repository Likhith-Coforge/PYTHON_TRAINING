scores = {
    "Anita": 92,
    "Ravi": 85,
    "Kiran": 76,
    "Zoya": 88
}

scores_list = list(scores.items())

scores_list[0] = scores_list[0][::-1]
scores_list[1] = scores_list[1][::-1]
scores_list[2] = scores_list[2][::-1]
scores_list[3] = scores_list[3][::-1]

scores = dict(scores_list)

user_input = int(input("Enter score: "))

print(scores.get(user_input,'Not found'))


"""
SOLUTION-2:

rev_scores = {}

for k,v in scores.items():
	rev_scores[v]=k

user_input = int(input("Enter score: "))

print(rev_scores.get(user_input,"Not found"))

"""