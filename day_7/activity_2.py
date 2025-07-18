num = int((temp := input()).isdigit() and temp or input("Enter a valid number[0-9]: "))
print(num%3==0 and "Jugs" or num)