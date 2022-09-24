# Chapter 4. Task 8. Sum of numbers
# Use f-string because they are faster and more convenient

# Get user data
print("Enter a series of positive numbers (negative number to signal the end of the series):")
num = int(input("Enter number: "))
total = 0

# Calculation
while num > 0:
	total += num
	num = int(input("Enter number: "))
	if num < 0:
		num = 0

# Return result
print(f"Sum of numbers: {total + num}")