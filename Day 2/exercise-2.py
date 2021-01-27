# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# In this exercise we are going to take a double digit number and add the two single numbers together.

# Here, we are separating the two integers as a string.
first_digit_number = two_digit_number[0]
second_digit_number = two_digit_number[1]

# Then we are turning the two string numbers into integers and adding them together.
result = int(first_digit_number) + int(second_digit_number)

# Printing out the result.
print( result )