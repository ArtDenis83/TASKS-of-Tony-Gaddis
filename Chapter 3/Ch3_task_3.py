# Task 3. Age Classifier

# Get user data
age = int(input("Enter age: "))

# Calculation
if age == 1 or age == 0:
	print("Infant")
elif age > 1 and age < 13:
	print("Child")
elif age >= 13 and age <= 20:
	print("Teenager")
elif age > 20:
	print("Adult")
else:
	print("Invalid value")