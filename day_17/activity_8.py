def is_prime(n):
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

def first_prime(n):
	for num in range(n+1,1000):
		if is_prime(num):
			return num
	return "Not found"

num = int(input("Enter a number: "))
print(first_prime(num))