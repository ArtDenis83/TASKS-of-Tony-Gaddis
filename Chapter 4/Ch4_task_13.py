# Chapter 4. Task 13.  Population
# Use f-string because they are faster and more convenient

# Get user data
num_units = int(input("Enter starting number of organisms: "))
gain_percent = int(input("Enter average daily population increase (as %): "))
days = int(input("Enter number of days the organisms will be left to multiply: "))

# Set values
percent = (gain_percent / 100)

# Show table header
print(" Day\tPopulation")
print("===================")

# Return result
print(f"  1 \t\t{num_units}")
for counter in range(2, days + 1, 1):
    gain = num_units * percent
    num_units += gain
    print(f"  {counter} \t\t{num_units:.2f}")
