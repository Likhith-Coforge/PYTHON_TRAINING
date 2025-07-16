print("Hello, world!")
print("Hello,\nworld!")

print("16","07","2025",sep="-")
print("Loading",end="... ")
print("Done")

name = "Anand"
marks = 95
print(f"Name: {name} Marks: {marks}")

print("start:",end=".....")
print("end")

x=input('enter number: ')
print(x)

x,y=input("enter two numbers: ").split()
print(x,y)

x,y,z=input('enter three numbers: ').split()
print(x,y,z)

u,v,w,x,y,z=input('enter 6 numbers: ').split()
print(u,v,w,x,y,z)

x,y=input('enter two numbers ').split(',')
print(x,y)

x,y=map(int,input('enter two numbers: ').split(','))
print(x,y)

a,b,c,d,e=map(int,input('enter 5 numbers: ').split(','))
print(a,b,c,d,e)

f1,f2,f3,f4=map(float,input('enter 4 numbers: ').split(','))
print(f1,f2,f3,f4)

x,y=map(float,input('enter two numbers: ').split(' '))
print(x,y)
print(type(x))
