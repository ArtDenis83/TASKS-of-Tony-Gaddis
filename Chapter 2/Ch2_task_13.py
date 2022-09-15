# Task 13. Planting Grapevines
# Calculation formula: V = (R-2*E) / S
# V - is the number of grapevines that will fit in the row;
# R - is the length of the row, in meters;
# Е - is the amount of space, in feet, used by an end-post assembly;
# S - is the space between vines, in meters.

# Get data from user
r = float(input("Please enter vine line length in meters: "))
e = float(input("Please enter end support space in meters: "))
s = float(input("Please enter space between vine in meters: "))

# Calculate
v = (r - 2 * e) / s

# Return result
print(f"Total number of vine: {v}")
