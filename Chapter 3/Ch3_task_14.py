# Task 14. Body Mass Index
# Use f-string because they are faster and more convenient


# Get user data
weight = float(input("Enter your weight (kilo): "))
height = float(input("Enter your height (cm): "))

# Set values
height_metr = height / 100
bmi = weight / height_metr**2

# Calculation and return result
print(f"Your body mass index (BMI): {bmi:.1f}")
if bmi < 18.5:
	print("You has underweight")
elif bmi >= 18.5 and bmi <= 25:
	print("You has optimal weight")
elif bmi > 25:
	print("You has overweight")