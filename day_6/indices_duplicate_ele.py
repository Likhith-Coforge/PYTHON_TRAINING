tpl = tuple(map(int,input().split(' ')))
key = int(input('Enter the element to be searched for its index: '))
idx = ""
rotation_val=0
for i in range(len(tpl)):
    if tpl[0]==key:
        idx+=str(rotation_val)
        idx+=" "
    rotation_val+=1
    tpl=tpl[1:]+tpl[:1]
print(f'Indices of {key} in {tpl} are {idx}')