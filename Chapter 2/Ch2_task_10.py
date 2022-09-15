# Task 10. Ingredients regulator.
# Use f-string because they are faster and more convenient

# Set value (glass per buns)
sugar_per_bun = 1.5 / 48
butter_per_bun = 1 / 48
flour_per_bun = 2.75 / 48

# Get data from user
buns_numbers = float(input("Please enter the number of buns: "))

# for more convenient perform calculations in f-string and return result
print(f"For {buns_numbers} buns you will need:")
print(f"{sugar_per_bun * buns_numbers:.1f} glass of sugar")
print(f"{butter_per_bun * buns_numbers:.1f} glass of butter")
print(f"{flour_per_bun * buns_numbers:.1f} glass of flour")
