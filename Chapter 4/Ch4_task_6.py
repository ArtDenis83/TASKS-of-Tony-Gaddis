# Chapter 4. Task 6. Celsius to Fahrenheit Table
# Use f-string because they are faster and more convenient

# Table header
print('Celsius to Fahrenheit Table')
print()
print(f"Temperature in C\t\tTemperature in F")
print("======================================")

# Calculation and return result
for C in range(0,21,1):
	F = (9 / 5) * C + 32
	print(f"\t\t{C}\t -------> \t{F:.1f}")