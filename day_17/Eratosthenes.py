# Sieve of Eratosthenes Algorithm

def get_prime_nums(n):
	""" This function takes an integer n and returns a list of all prime numbers up to n(inclusive) using the Sieve of Eratosthenes algorithm"""
	
	new_list = list(range(2,n+1))
	
	for idx in range(len(new_list)//2):
		for num in new_list[idx+1:]:
			if num%new_list[idx] == 0:
				new_list.remove(num)
		print(new_list)
	print(new_list)

num = int(input("Enter a integer: "))
get_prime_nums(num)
	
	