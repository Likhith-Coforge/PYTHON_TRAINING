val = int((temp := input()).isdigit() and temp or input("Enter a valid number[0-9]: "))
print((val%5==0 and val%3==0 and "Jugs Mugs") or (val%5==0 and "Mugs") or (val%3==0 and "Jugs") or val)