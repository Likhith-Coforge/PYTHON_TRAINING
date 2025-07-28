# EB Bill

previous_meter_reading = float(input("Enter your previous meter reading: "))

current_meter_reading = float(input("Enter your current meter reading: "))

total_bill = 0

meter_diff = (current_meter_reading - previous_meter_reading)

if meter_diff > 1000:
	total_bill += meter_diff * 11.80
elif meter_diff > 800:
	total_bill += meter_diff * 10.70
elif meter_diff > 600:
	total_bill += meter_diff * 9.65
elif meter_diff > 500:
	total_bill += meter_diff * 8.55
elif meter_diff > 400:
	total_bill += meter_diff * 6.45
elif meter_diff > 0:
	total_bill += meter_diff * 4.80
else:
	total_bill += 0

print(f"Your total eb bill for the current month is {total_bill} rupees.")