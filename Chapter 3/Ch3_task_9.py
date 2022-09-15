# Task 9. Roulette Wheel Colors
"""
color = 0 green
color = 1 red
color = 2 black
color = 999 invalid number
"""
# Set values
color = True

# Get user data
number = int(input("Enter a pocket number in range of 0 through 36: "))

# Calculation
if number < 0 or number > 36:
	color = 999
elif number == 0:
	color = 0
elif number >= 1 and number <= 10:
	even_odd = number % 2
	if even_odd == 0:
		color = 2
	elif even_odd == 1:
		color = 1
elif number >= 11 and number <= 18:
	even_odd = number % 2
	if even_odd == 0:
		color = 1
	elif even_odd == 1:
		color = 2
elif number >= 19 and number <= 28:
	even_odd = number % 2
	if even_odd == 0:
		color = 2
	if even_odd == 1:
		color = 1
elif number >= 29 and number <= 36:
	even_odd = number % 2
	if even_odd == 0:
		color = 1
	if even_odd == 1:
		color = 2

# Return result
if color == 0:
	print ("Pocket is green")
elif color == 1:
	print("Pocket is red")
elif color == 2:
	print("Pocket is black")
else:
	color = 999
	print("Invalid number")