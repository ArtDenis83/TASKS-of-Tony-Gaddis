# Task 16. February Days
# Use f-string because they are faster and more convenient


# Get user data
year = int(input("Enter year: "))

# Calculation and return result
if year % 100 == 0 and year % 400 == 0:
	print(f"In {year} February has 29 days, leap year.")
elif year % 100 !=0 and year % 4 == 0:
	print(f"In {year} February has 29 days, leap year.")
else:
	print(f"In {year} February has 28 days, not leap year.")