# Chapter 4. Task 4. Error collector
# Use f-string because they are faster and more convenient

# Set value
DAYS = 3
total_errors = 0

# Get user data and calculation
for counter in range(DAYS):
	counter += 1
	print(f"Day {counter}:")
	data = int(input("Enter the number of errors: "))
	total_errors += data

# Return result
print("===========================================")
print (f"The number of days during which monitoring was performed: {DAYS}"\
	   f"\nTotal number of errors for the specified period: {total_errors}")