# Chapter 4. Task 12. Calculating the Factorial of a Number.
# Use f-string because they are faster and more convenient

# Get user data
num = int(input("Enter a non-negative integer: "))

# Calculation
while num <= 0:
	num = int(input("Enter a non-negative integer: "))
total = 1
for counter in range(1, num+1, 1):
	x = 1 * counter
	total *= counter

# Return result
print(f"The factorial of {num} is {total}")