def fibonacci():
	t0 = 0
	t1 = 1
	print(t0,end=',')
	print(t1,end=',')
	while True:
		t2 = t0+t1
		yield t2
		t0 = t1
		t1 = t2
fib = fibonacci()
print(next(fib),end=',')
print(next(fib),end=',')
print(next(fib),end=',')
print(next(fib),end=',')
print(next(fib),end=',')
print(next(fib),end=',')
print(next(fib),end=',')
print(next(fib),end=',')
print(next(fib))