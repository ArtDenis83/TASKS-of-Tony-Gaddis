# Task 12. Software Sales
# Use f-string because they are faster and more convenient


# Get user data
soft_pack = int(input("Enter purchased software packages: "))

# Set values
pack_cost = 99

# Calculation discount
if soft_pack <= 9:
	disc = 0
elif soft_pack >=10 and soft_pack <=19:
	disc = 0.1
elif soft_pack >=20 and soft_pack <= 49:
	disc = 0.2
elif soft_pack >=50 and soft_pack <= 99:
	disc = 0.3
elif soft_pack > 99:
	disc = 0.4

# Calculation total amount of the purchase after discount
total_cost = soft_pack * pack_cost
cost_with_disc = total_cost - (total_cost * disc)
disc_sum = total_cost - cost_with_disc

# Return result
if disc > 0:
	print(f"Your discount {disc * 100:.0f}%, amount of the discount $ {disc_sum:.2f}")
else:
	print(f"You have no discount")

print (f"Total amount of the purchase with discount $ {cost_with_disc:.2f}")