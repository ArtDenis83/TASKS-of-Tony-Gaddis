# Task 11. Students percentage of both sexes
# Use f-string because they are faster and more convenient

# Get data from user
male = int ( input("Please enter the number of male students: "))
female = int ( input("Please enter the number of female students: "))

# Calculate
students_sum = male + female
male_percent = male / students_sum
female_percent = female / students_sum

# Return result
print(f"Male students percent is: {male_percent:.0%}")
print(f"Female students percent is: {female_percent:.0%}")
