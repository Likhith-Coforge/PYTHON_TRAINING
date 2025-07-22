data = [('A',1,2),('B',3),('C',4,5,6),('D',),('E',7,8)]

ordered_list = sorted(data,key=len)

result = []

for val in ordered_list:
	result.append(val[0])

print(result)
