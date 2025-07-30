names = ['Alice','Bob','Charlie']
marks = [85, 90, 88]
grades = ['B','A','A']

for line_num,name,mark,grade in zip([1,2,3],names,marks,grades):
	print(line_num,name,mark,grade,sep=",")

