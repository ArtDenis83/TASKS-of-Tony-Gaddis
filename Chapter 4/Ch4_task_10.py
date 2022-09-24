# Chapter 4. Task 10.  Tuition Increasе.
# Use f-string because they are faster and more convenient

# Set value 
BASE_SIMESTER_TUITION = 8000
YEAR = 5
COST_INCREASE = 1.03

# Show table header
print (f"year of study \tSemester cost")
print("=================================")

# Return first year row without increase
year_cost = BASE_SIMESTER_TUITION * 2
print(f"\t  1\t\t\t$ {year_cost / 2}")

# Calculation
total = 0
for year_count in range(2, YEAR+1, 1):
	year_cost = (year_cost * COST_INCREASE)
	simester_cost = year_cost / 2
	# Return result at each iteration
	print(f"\t  {year_count}\t\t\t$ {simester_cost:.2f}")