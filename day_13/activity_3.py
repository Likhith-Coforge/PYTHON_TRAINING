std_score = int(input("Enter your score: "))

grade = ""

score_dict = {'A':'Excellent work!','B':'Good Job!','C':'Satisfactory'
,'D':'Needs improvement','F':'Please study more'}

if std_score >= 90:
	grade += 'A'
elif std_score >= 80 and std_score <= 89:
	grade += 'B'
elif std_score >= 70 and std_score <= 79:
	grade += 'C'
elif std_score >= 60 and std_score <= 69:
	grade += 'D'
else:
	grade += 'F'

print(f'Grade: {grade}, {score_dict[grade]}')
	