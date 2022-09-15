# Task 6. Sales tax.
# Use f-string because they are faster and more convenient
# Federal tax = 5%, regional tax = 2.5%

# Get data from user
purchase_cost = float(input("Please, enter purchase cost: $ "))

# Calculating of the tax amount
fed_tax = purchase_cost * 0.05
reg_tax = purchase_cost * 0.025

# Calculating purchase cost with taxes
total_purch_cost = purchase_cost + fed_tax + reg_tax

# Return result
print(f"The purchase cost is: $ {purchase_cost}")
print(f"Federal purchase tax is: $ {fed_tax:.2f}")
print(f"Regional purchase tax is: $ {reg_tax:.2f}")
print(f"Purchase cost, including all taxes is: $ {total_purch_cost:.2f}")
