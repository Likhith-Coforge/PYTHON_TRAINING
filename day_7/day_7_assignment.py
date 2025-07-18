# take input from the user, if its a non-digit then ask the user for the input again to enter a valid number

val = int((num := input("Enter the number: ")).isdigit() and num or input("Enter numeric value: "))

""" print jugs if num%3==0 
    print mugs if num%5==0
    print jugs mugs if num%5==0 and num%3==0
    print bugs if num%7==0
    print mugs bugs if num is divisible by 5,7
    print jugs bugs if num is divisible by 3,7
    print jugs mugs bugs if num is divisible by 3,5,7
"""

print((val%7==0 and val%5==0 and val%3==0 and "Jugs Mugs Bugs") or (val%7==0 and val%5==0 and "Bugs Mugs") or  (val%7==0 and val%3==0 and "Bugs Jugs") or (val%5==0 and val%3==0 and "Jugs Mugs") or (val%7==0 and "Bugs") or (val%5==0 and "Mugs") or (val%3==0 and "Jugs") or val)