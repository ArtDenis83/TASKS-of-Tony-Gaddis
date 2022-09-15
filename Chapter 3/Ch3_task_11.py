# Task 11. Book Club Points

# Get user data
books = int(input("Enter the number of purchased books: "))

# Calculation and return result
if books <= 1:
	print("Earns: 0 points")
elif books >= 2 and books < 4:
	print("Earns: 5 points")
elif books >=4 and books < 6:
	print("Earns: 15 points")
elif books >=6 and books < 8:
	print("Earns: 30 points")
elif books >=8:
	print("Earns: 60 points")