n = int(input("Enter an integer: "))
loop_count = 0

while n>=0:
	n -= 3
	loop_count += 1

print(f"Loop ran for {loop_count} times")