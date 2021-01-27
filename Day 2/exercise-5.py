#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal

#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip Calculator!")
# Grabbing input for the bill total.
bill_total = input("How much is the bill? ")

# Grabbing input for how many people are in the group.
num_people = input("How many people are in the group? ")

# Let's ask how much we want to tip.
tip = input("How much do you want to tip? ")

# We need to convert the strings, as numbers so we can do the math.
new_bill_total = float(bill_total)
new_num_people = int(num_people)
new_tip = int(tip)

# Let's do some math!!
tip_percentage = new_tip / 100
total_tip = new_bill_total * tip_percentage
total_bill = new_bill_total + total_tip
result = total_bill / new_num_people

# We're going to round the answer to the nearest second decimal.
final_result = "{:.2f}".format(result)

# Print the result
print( f" The total everyone pays is {final_result}" )