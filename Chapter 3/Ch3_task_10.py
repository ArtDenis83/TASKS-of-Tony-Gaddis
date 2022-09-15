# Task 10. Money Counting Game

# Get user data
coin_1 = int(input("Select the quantity of one cent coin: "))
coin_5 = int(input("Select the quantity of five cent coin: "))
coin_10 = int(input("Select the quantity of ten cent coin: "))
coin_25 = int(input("Select the quantity of twenty-five cent coin: "))

# Show user values
print ("Your choise:")
print ("1 cent: ", coin_1, "pcs")
print ("5 cent: ", coin_5, "pcs")
print ("10 cent: ", coin_10, "pcs")
print ("25 cent: ", coin_25, "pcs")

# Set values
dollar = 100
cent_1 = 1
cent_5 = 5
cent_10 = 10
cent_25 = 25

# Calculation
total_cent_1 = coin_1 * cent_1
total_cent_5 = coin_5 * cent_5
total_cent_10 = coin_10 * cent_10
total_cent_25 = coin_25 * cent_25
total_sum = total_cent_1 + total_cent_5 + total_cent_10 + total_cent_25

# Return result
if total_sum == dollar:
	print("CONGRATULATIONS!!! YOU WIN!!!")
elif total_sum > dollar:
	print("Total value of the coins is more than one dollar")
elif total_sum < dollar:
	print("Total value of the coins is less than one dollar")