# Task 5. Mass and Weight
# Use f-string because they are faster and more convenient

# Get user data
weigth_kg = float(input("Enter an object’s mass (kilograms): "))

# Calculation
weight_N = weigth_kg * 9.8
w = weight_N

# Return result
if w < 100:
	print("It is too light")
elif w > 500:
	print("It is too heavy")
elif w >= 100 and w <=500:
	print(f"Weight in newtons: {w:.2f}")