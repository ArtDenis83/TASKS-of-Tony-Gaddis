# Task 8. Hot Dog Cookout Calculator

# Set global variables
SAUSAGE_PACK = 10
BUN_PACK = 8
sausage_packages = True

# Auxiliary variables for sausages and buns
aux_var_sausage = True 
aux_var_buns = True

# Get user data
persons = int(input("Enter the number of people attending the cookout: "))
hotdog = int(input("Enter the number of hot dogs each person will be given: "))

# Calculation of the total numbers of hot dogs
total_hotdogs = persons * hotdog
t = total_hotdogs

# Calculation of the sausages package numbers
if t <= SAUSAGE_PACK:
	sausage_packages = 1
	sausage_leftover = SAUSAGE_PACK - t
elif t > SAUSAGE_PACK:
	aux_var_sausage = t % SAUSAGE_PACK
	if aux_var_sausage == 0:
		sausage_packages = t / SAUSAGE_PACK
	elif aux_var_sausage >=1:
		sausage_packages = t / SAUSAGE_PACK +1

sausage_leftover = int(sausage_packages) * SAUSAGE_PACK - t

# Calculation of the bun packages
if t <= BUN_PACK:
	bun_packages = 1
	bun_leftover = BUN_PACK - t
elif t > BUN_PACK:
	aux_var_buns = t % BUN_PACK
	if aux_var_buns == 0:
		bun_packages = t // BUN_PACK
	elif aux_var_buns >=1:
		bun_packages = t // BUN_PACK + 1

bun_leftover = int(bun_packages) * BUN_PACK - t

# Return result
# Use integer to discard the decimal fractions obtained during calculations
print("Required numbers of sausage packages: ", int(sausage_packages))
print("Required numbers of bun packages: ", int(bun_packages))
print("Left over of sausages in package: ", int(sausage_leftover))
print("Left over of buns in package: ", int(bun_leftover))