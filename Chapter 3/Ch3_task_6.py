# Task 6. Magic Dates

# Get user data
day = int(input("Enter day (two digits) : "))
month = int(input("Enter month in numeric form: "))
year = int(input("Enter two-digit year: "))

# Calculation
a = day * month

#Return result
if a == year:
	print("!!! This is a magic date !!!")
elif a != year:
	print("Regular date, nothing special or magical")