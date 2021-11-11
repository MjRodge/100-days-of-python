# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
months_if_ninety = 90*12
weeks_if_ninety = 90*52
days_if_ninety = 90*365

age = int(age)
current_days = age*365
current_weeks = age*52
current_months = age*12

days_remaining = days_if_ninety-current_days
weeks_remaining = weeks_if_ninety-current_weeks
months_remaining = months_if_ninety-current_months
# using f-strings
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months remaining")