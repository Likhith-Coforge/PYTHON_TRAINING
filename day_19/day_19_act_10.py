with open('quote.txt','r') as file:
	content = file.readlines()

print(content)

with open('reversed.txt','w') as f:
	f.write("".join(content[::-1]))

with open('reversed.txt','r') as f1:
	text = f1.readlines()

print(text)