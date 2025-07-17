# print the index of the last element.
t1 = tuple(map(int,input().split(' ')))

print(len(t1)-1)

print(t1.index(t1[-1]))
