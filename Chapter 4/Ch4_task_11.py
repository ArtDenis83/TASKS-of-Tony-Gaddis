# Chapter 4. Task 11.  Weight loss.
# Use f-string because they are faster and more convenient

# Set values
LOSE_WGHT = 1.5

# Get user data
wght = float(input("Enter your weight: "))

# Show table header
print(" Month\tWeight")
print("================")

# Calculation
for counter in range(0, 7, 1):
	lose_wght = LOSE_WGHT * counter
	# Return result at each iteration
	print(f"   {counter}  \t{wght - lose_wght:.2f}")