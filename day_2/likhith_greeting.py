# Task2: Decode the Message:

data="Luna42Kai3.14True#Knight"

name = data[0:4] # extracting Luna from the string data

int_data = data[4:6] # extracting 42 from data and storing it in a temp variable
int_data_add = int(int_data)+8

float_data_num = data[9:13] # extracting 3.14 from data and storing it in a temp variable
float_data_mul = float(float_data_num)*2

title_data = data[-6:] # Slicing "Knight" using negative index
reverse_title_data = title_data[::-1] # Reversing the extracted title

print("Name: "+name.upper())
print(f'{int_data} + 8 = {int_data_add}')
print(f'{float_data_num} * 2 = {float_data_mul}')
print("Reversed Title: "+reverse_title_data)

