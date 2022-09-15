# Task 9. Celsius to Fahrenheit converter
# Use f-string because they are faster and more convenient

# Get data from user
temp_c = float(input("Enter temperature in Celsius: "))

# Calculation
temp_f = (9 / 5) * temp_c + 32

# Return result
print(f"Temperature in Fahrenheit: {temp_f:.1f}")
