fruit_prices = {'elppa': 100, 'ananab': 50, 'elppa dratsuc': 200}

fruit_input = input("Enter the fruit name: ")

print(fruit_prices.get(fruit_input[::-1],"Invalid fruit name"))