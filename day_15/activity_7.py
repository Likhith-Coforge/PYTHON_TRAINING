num = int(input("Enter a integer: "))

for m in range(1,num):
	count = 0
	for n in range(2,m+1):
		if m%n == 0:
			count += 1
	if count==1:
		print(m,end=" ")