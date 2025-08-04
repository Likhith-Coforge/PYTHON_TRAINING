raw_guests = [' alice ','','Bob','ALICE','  bob   ',' Eve ','eve',' ','       ANAND']

raw_guests_1 = [name for name in raw_guests if len(name)>1]

raw_guests_2 = [name.strip() for name in raw_guests_1]

raw_guests_3 = [name.capitalize() for name in raw_guests_2]

final_result = {name:len(name) for name in raw_guests_3}

print(raw_guests_1)
print(raw_guests_2)
print(raw_guests_3)
print(final_result)

