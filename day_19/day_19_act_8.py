with open('quote.txt','w') as file:
	file.write("All shining glitters are not gold.\n")

with open('quote.txt','r') as file_1:
	text = file_1.read()
	print(text)