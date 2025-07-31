import random

computers_choice = random.randint(1,100)

print("I am ready with a number. Now its your turn to guess it.")

user_guess = int(input("Enter your guess(for playing the game) or -1(for quitting): "))

while True:
	if user_guess == -1:
		break
	elif user_guess == computers_choice:
		print("Hey your guess is Correct!")
		break
	elif user_guess > computers_choice:
		print("Your guess is Too high")
		user_guess = int(input("Enter your guess: "))
	elif user_guess < computers_choice:
		print("Your guess is Too low")
		user_guess = int(input("Enter your guess: "))
		