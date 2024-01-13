# one_year = 52
# year_90_in_weeks = one_year * 90
# present_age = int(input('Enter age: ')) * 52

# weeks_left = year_90_in_weeks - present_age

# print('You have', weeks_left, 'weeks left')
# print(year_90_in_weeks)

# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7


print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? $'))
percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
tip = total_bill * (percentage/100)

sum_totalbill_withtip = tip + total_bill
pay_per_person = sum_totalbill_withtip / people

print('Each person should pay: $', round(pay_per_person, 2))