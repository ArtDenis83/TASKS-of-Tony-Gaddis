# Task 18. Restaurant Selector

# Get user data
vegetarian = input("Is anyone in your party a vegetarian? (yes/no): ")
vegan = input("Is anyone in your party a vegan? (yes/no): ")
gluten = input("Is anyone in your party gluten-free? (yes/no): ")

# Calculation
if vegetarian == "yes":
	vegetarian = 1
else:
	vegetarian = 0
if vegan == "yes":
	vegan = 1
else:
	vegan = 0
if gluten == "yes":
	gluten = 1
else:
	gluten = 0

# Return result
print("Here are your restaurant choices:")

# Calculation and return result
if vegetarian == 0 and vegan == 0 and gluten == 0:
	print("Joe’s Gourmet Burgers ")
if vegetarian >= 0 and vegan == 0 and gluten >= 0:
	print("Main Street Pizza Company ")
if vegan >= 0 and vegan >= 0 and gluten >= 0:
	print ("Corner Cafe ")
	print ("The Chef’s Kitchen")
if vegetarian >= 0 and vegan == 0 and gluten == 0:
	print ("Mama’s Fine Italian")