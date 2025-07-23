fruit_prices = {'elppa': 100, 'egnaro': 150, 'ananab': 200}

# Extracting the keys from fruit_prices dict and sorting them
fruits_list = [''.join(sorted(fruit)) for fruit in fruit_prices.keys()]

# Replacing the earlier keys with the new sorted keys into fruit_prices dict
fruit_prices = dict(zip(fruits_list,fruit_prices.values()))

user_input = ''.join(sorted(input("Enter the fruit name: ")))

print(fruit_prices.get(user_input,"Not found"))