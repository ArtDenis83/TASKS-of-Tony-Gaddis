# Chapter 4. Task 7. Pennies for pay
# Use f-string because they are faster and more convenient

# Show description
print("Program calculate amount of money a person would earn over a period of time. Its double each day")
print("======================================================================")
print()

# Get user data
days = int(input("Enter number of days): "))

# Validate input data
while days <= 0:
	print("Number of days cannot be less than 1")
	days = int(input("Enter another number of days: "))
while days > 55:
	print("If you enter more than 55 days, the total amount of earnings will exceed 360 trillion dollars,\
          \nand it will exceed the value of all world's wealth.")
	days = int(input("Enter another number of days: "))

# Calculation
counter = 0
iteration_salary = 0.01
print('=========================')
print(f"Number\t\tAmount\n  of\t\t per\n  day\t\t day")
print("=======================")
print(f"   {counter+1}\t->\t${iteration_salary}")
total = iteration_salary

# Return result
if days > 1:
	for counter in range(1,days,1):
		iteration_salary = iteration_salary * 2
		print(f"   {counter + 1}\t->\t${iteration_salary:.2f}")
		total += iteration_salary
	print(f"Total pay at the end of period: ${total:.2f}")
else:
	print(f"Total pay at the end of period: ${total:.2f}")