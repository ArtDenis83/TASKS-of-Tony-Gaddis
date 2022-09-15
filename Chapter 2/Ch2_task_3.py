# Task 3. Calculating of the area of the land plot
# Use f-string because they are faster and more convenient

#Get data from user
sq_meter_sum = float(input(f"Enter the total number of land square meters: "))

#Calculate
acr_sum = sq_meter_sum / 4047

#Return result
print(f"The total numbers of acres: {acr_sum:.2f}")
