# Task 2. Sales forecast
# Use f-string because they are faster and more convenient

#Get data from user
planning_sales = float(input(f"Enter the planned amount of total sales: $ "))

#Calculate
planning_profit = (planning_sales * 23) / 100

#Return result
print(f"The profit will be: $ {planning_profit:.2f}")
