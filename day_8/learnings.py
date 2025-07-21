t1 = ([1,2,(3,4)],)

print(t1)
print(type(t1[0][2]))


t1 = (1,2) # declaring tuple t1
t2 = ('*',) # declaring tuple t2

t3 = t1+t2 # tuple creation using concatenation operator on existing tpls
t4 = t3*2 # tuple creation using repetition operator on existing tpl
print(t3) # display tpl3
print(t4) # display tpl4

# tuple creation combining all three operations in a single line of code
t5 = t4 + ('*' in t4 and f'* is repeated {t4.count('*')} in tuple 4',10 in t4 or 10)*2
print(t5)


# Unpacking tuple elements
a, b = (100,200)
print(a,b)

# Unpacking tuple elements dynamically
v1, v2, v3 = (10,20,int(input()))
print(v1,v2,v3)

# Unpacking tuple elements(iterable) dynamically
a,b,c = (1,2,list(map(int,input().split(" "))))
print(a,b,c)
