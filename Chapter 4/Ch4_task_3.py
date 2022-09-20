# Chapter 4. Task 3. Budget analysis
# Use f-string because they are faster and more convenient

# Get user data
budget = float(input("Enter your monthly budget: "))
expense = float(input("Enter amount of separate expense item, enter zero (0) if not: "))

# Calculation
total_expense = 0
while expense > 0:
	total_expense += expense
	expense = float(input("Enter the amount of a separate expense item, enter zero (0) if not: "))
balance = budget - total_expense

# Return result
print ("*******************************************************************************")
if balance >=0:
	print (f"End of the month balance, including all expenses: $ {balance}")
elif balance < 0:
	print (f"Formed a debt. You balance: $ {balance}")