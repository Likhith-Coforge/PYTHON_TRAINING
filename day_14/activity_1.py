invited_people = {'Alice','Bob','Charlie'}

arrived_people = {'Alice','Charlie','Diana','John','kali'}

unexpected_guests = arrived_people - invited_people

if unexpected_guests:
	print(f'Unexpected guests arrived:')
	print(*unexpected_guests)