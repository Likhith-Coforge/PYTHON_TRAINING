email_guests = {'a','b','c'}
phone_guests = {'b','c','d'}
blocked_guests = {'c','d','e'}

final_guests = ((email_guests & phone_guests) - blocked_guests) | (blocked_guests - email_guests - phone_guests)

print(final_guests)