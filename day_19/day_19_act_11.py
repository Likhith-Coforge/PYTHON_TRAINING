with open('guests.txt','r') as file:
	text = file.read()

print(f"Existing guests: \n{text}")

new_guest = input("Enter new guest: ")

with open('guests.txt','a') as f:
	f.write(f"\n{new_guest}")

