# Task 3.Day of week

day_of_week = int(input("Please enter a valid day of week (1-7)"))
if day_of_week == 1:
	print ("monday")
elif day_of_week == 2:
	print ("tuesday")
elif day_of_week == 3:
	print ("wednesday")
elif day_of_week == 4:
	print ("thursday")
elif day_of_week == 5:
	print ("friday")
elif day_of_week == 6:
	print ("saturday")
elif day_of_week == 7:
	print ("sunday")
else:
	if day_of_week <=0 or day_of_week >=8:
		print ("Out of range")