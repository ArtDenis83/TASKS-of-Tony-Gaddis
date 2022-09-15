# Task 13. Shipping Charges

# Get user data
weight = float(input("Enter the weight of a package (in gramms): "))

# Rate calculation
if weight <= 200:
	rate = 150
elif weight > 200 and weight <= 600:
	rate = 300
elif weight > 600 and weight <= 1000:
	rate = 400
elif weight > 1000:
	rate = 475

cost = (weight / 100) * rate

# Return result
print(f"The shipping charges: {cost:.0f} rubbles")