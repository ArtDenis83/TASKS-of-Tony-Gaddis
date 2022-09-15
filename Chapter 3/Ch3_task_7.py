# Task 7. Color mixer

# add values
red = 1
blue = 2
yellow = 3

# Get user data
a = input("Enter first color (red, blue or yellow): ")

# Conversion of user data
if a == "red":
	color1 = 1
elif a == "blue":
	color1 = 2
elif a == "yellow":
	color1 = 3
else:
	print("Wrong color, or invalid format. Check the spelling\n (red, blue or yellow)")

# Get user data
b = input("Enter second color (red, blue or yellow): ")

# Conversion of user data
if b == "red":
	color2 = 1
elif b == "blue":
	color2 = 2
elif b == "yellow":
	color2 = 3
else:
	print("Wrong color, or invalid format. Check the spelling\n (red, blue or yellow)")

# Calculation
if color1 == 1 and color2 == 2:
	print("When you mix red and blue, you get purple")
elif color1 == 1 and color2 == 3:
	print("When you mix red and yellow, you get orange")
elif color1 == 2 and color2 == 3:
	print("When you mix blue and yellow, you get green")
elif color1 == color2:
	print("Mixing the same shades, the color will not change")
else:
	print("Wrong color, or invalid format. Check the spelling\n (red, blue or yellow)")
