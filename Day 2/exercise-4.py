# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Writing an app that calculates how many days, weeks and months you have left until you reach 90 years old.

# Converting age into a string.
new_age = int(age)

# 90 minus the input age.
years_left = 90 - new_age
# Calculating the days you have left.
days_left = years_left * 365
# Calculating the weeks you have left.
weeks_left = years_left * 52
# Calculating the months you have left.
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")