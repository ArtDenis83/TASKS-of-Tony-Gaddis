# Chapter 4. Task 4. Distance traveled
# Use f-string because they are faster and more convenient

# Get user data
speed = int(input("Enter car speed (km/h): "))
time = int(input("Enter travel time (hours): "))

# Table header
print(f"Hour\tDistance traveled")
print("----------------------------")

# Calculation and return result
distance = 0
for counter in range(1, time + 1, 1):
    distance = speed * counter
    print(f"{counter}\t\t{distance}")
