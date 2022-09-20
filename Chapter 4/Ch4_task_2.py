# Chapter 4. Task 2. Calories burned
# Use f-string because they are faster and more convenient

# Set value
kkal = 4.2
start_time = 10
end_time = 30

# Calculation and return result
for counter in range(start_time, end_time + 1,5):
	burn = kkal * counter
	print(f"In {counter} minutes of running, {burn:.0f} calories are burned")