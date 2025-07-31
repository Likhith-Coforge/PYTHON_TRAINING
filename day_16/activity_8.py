def f(x,lst = list()):
	lst.append(x)
	temp = lst.copy()
	lst.clear()
	return temp

print(f(1))
print(f(2))
print(f(3))
print(f(4))