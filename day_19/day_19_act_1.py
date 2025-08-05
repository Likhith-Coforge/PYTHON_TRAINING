from random import randint

def flip_biased_coin():

	rand_num = randint(1,10)

	return "Heads" if rand_num <= 7 else "Tails"

print(flip_biased_coin())