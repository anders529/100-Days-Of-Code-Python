# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# We are writing an app that calculates your BMI.

# Converting strings into floating integers.
new_height = float(height)
new_weight = float(weight)

# Calculating the results so that we get the proper BMI.
result = new_weight / new_height ** 2

# Converting the floating integer into a regular integer so there is no decimal.
print( int(result) ) 