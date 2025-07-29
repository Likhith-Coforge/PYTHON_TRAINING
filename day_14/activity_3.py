user_age = int(input("Enter your age: "))

ticket_price = user_age < 12 and "$100" or "$200"

print(f'Ticket Price: {ticket_price}')