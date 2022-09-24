# Chapter 4. Task 9.  Ocean Levels.
# Use f-string because they are faster and more convenient


# Set value. Assuming the ocean’s level is currently rising at about 1.6 millimeters per year
RISE = 1.6

# Show table header
print(f" Year\t  Risen (mm)")
print("=====================")

# Calculation
total = 0
for counter in range(1, 26, 1):
    total += RISE
    # Return result at each iteration
    print(f"  {counter} \t\t{total:.1f}")
