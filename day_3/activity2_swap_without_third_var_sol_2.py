x = 5
y = 7

# Solution-2

print(f'Initially: x={x} and y={y}')

y = x * y
x = int(y / x)
y = int(y / x)

print(f'After Swapping: x={x} and y={y}')

