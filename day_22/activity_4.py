employee = "Abi"
hours_worked = 45.75
hourly_rate = 350.50
bonus = 1500
target_hours = 40

print(f"{12*"*"} Employee Report {12*"*"}")
print()
print(f"{5*" "} Employee Name: {17*" "}{employee}")
print(f"{6*" "} Hours Worked: {15*" "}{hours_worked}")
print(f"{6*" "} Target Hours: {18*" "}{target_hours}")
print(f"{9*" "} Overtime : {16*" "}{hours_worked-target_hours}")
print(f"{9*" "} Total Pay: $00{hourly_rate*45.75+bonus}")