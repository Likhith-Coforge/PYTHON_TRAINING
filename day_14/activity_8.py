user_num = int(input("Enter a 4-digit number: "))

# solution -1

user_num = str(user_num)

first_two_digit_sum = int(user_num[0]) + int(user_num[1])
last_two_digit_sum = int(user_num[2]) + int(user_num[3])

# solution - 2

last_two_digit_sum = 0
last_two_digit_sum += user_num%10
user_num //= 10
last_two_digit_sum += user_num%10
user_num //= 10

first_two_digit_sum = 0
first_two_digit_sum += user_num%10
user_num //= 10
first_two_digit_sum += user_num

both_sum_equality_check = first_two_digit_sum == last_two_digit_sum

if both_sum_equality_check:
	print("Lucky")
else:
	print("Unlucky")

