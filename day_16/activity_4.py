nums_list = list(map(int,input("Enter the numbers: ").split(" ")))

print(sorted(nums_list,key=abs))