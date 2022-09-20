# Chapter 5. Task 5. Average thickness of rainfall
# Use f-string because they are faster and more convenient

# Table header
print("Average thickness of rainfall")
print()

# Get user data
period = int(input("Enter the number of years: "))
print("===================================")

# Calculation and get another user data
total_precipitation = 0
for year in range(1, period + 1, 1):
    for month in range(1, 13, 1):
        print(f"Year: {year}\tmonth: {month}")
        precipitation = int(input("Enter precipitation amount (mm): "))
        total_precipitation += precipitation

# Return result
print("===================================")
print(f"Number of observation months: {period * 12}")
print(f"Total amount of rainfall: {total_precipitation} mm")
print(f"Average thickness of rainfall per month: {total_precipitation / (period * 12):.2f} mm")
