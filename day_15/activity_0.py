user_score = int(input("Enter your score: "))

grade = (user_score > 90 and "A") or (user_score > 80 and "B") or (user_score > 70 and "C") or (user_score > 60 and "D") or (user_score >= 0 and "E")

grade_dict = {"A": "Excellent job!","B":"Very good","C":"Good","D":"Need improvement","E":"Study very hard"}

result = grade_dict.get(grade,"Invalid Score")

if result:
	print(result)