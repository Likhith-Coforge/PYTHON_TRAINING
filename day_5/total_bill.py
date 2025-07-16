quantity, price = map(float,input('Enter the quantity and price: ').split(' '))

total_bill = quantity*price

print(f'Total Bill: ${total_bill}')