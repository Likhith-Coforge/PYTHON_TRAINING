with open('quote.txt','a') as file:
	file.write("\nPractice makes man perfect.")

with open('quote.txt','r') as file_1:
	text = file_1.read()
	print(text)