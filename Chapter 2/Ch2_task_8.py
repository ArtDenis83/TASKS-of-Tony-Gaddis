# Task 8. Tip, tax and total amount
# Use f-string because they are faster and more convenient

# Get data from user
meal_cost = float(input("Please enter the cost of the meal: "))

# Calculate tax and tips
tax = meal_cost * 0.07
tips = meal_cost * 0.18

# Return result
print(f"Tax amount is: {tax:.2f}")
print(f"Tips amount is: {tips:.2f}")
print(f"Total price with tips and taxes is: ${meal_cost + tax + tips:.2f}")
