# Task 4. Total sales
# Use f-string because they are faster and more convenient

# Get data from user
milk = float(input("Enter milk price: "))
butter = float(input("Enter butter price: "))
broad = float(input("Enter broad price: "))
meat = float(input("Enter meat price: "))
cheese = float(input("Enter cheese price: "))

# Calculate
purchase_summary = milk + butter + broad + meat + cheese
total = purchase_summary + (purchase_summary * 0.07)

# Return result
print(f"Amount of all purchases, including tax is: $ {total:.2f}")
