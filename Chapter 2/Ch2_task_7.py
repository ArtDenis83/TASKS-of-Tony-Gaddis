# Task 7.  Gasoline consumption per kilometers traveled.
# Use f-string because they are faster and more convenient

# Get data from user
fuel_consumption = float(input("Enter the numbers of liters, spent during the journey: "))
distance = float(input("Enter traveled distance in kilometers: "))

# for more convenient perform calculations in f-string
# return result
print(f"Gasoline consumption is: {(fuel_consumption / distance)*100:.2f} liters per 100 km")
