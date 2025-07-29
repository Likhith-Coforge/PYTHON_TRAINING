num1, num2 = map(int,input("Enter two integers separated by a space: ").split(" "))

print(f'Before swapping: num1 = {num1}, num2 = {num2}')

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print(f'After swapping: num1 = {num1}, num2 = {num2}')
