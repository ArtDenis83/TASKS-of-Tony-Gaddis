# Task 15. Time Calculator
# Use f-string because they are faster and more convenient


# Get user data
total_seconds = float(input('Enter number of seconds: '))

# Calculate hours
hours = (total_seconds // 3600) % 24
# Calculate minutes
minutes = (total_seconds // 60) % 60
# Calculate seconds
seconds = total_seconds % 60
# Calculate days
days = ((total_seconds // 3600) // 24) % 365
# Calculate years
years = (((total_seconds // 3600) // 24) // 365)

# Return result
if total_seconds <= 60:
    print(f"Entered number of seconds contains:\
    \nminutes: {minutes:.0f}\
    \nseconds: {seconds:.0f}")
elif total_seconds > 60 and total_seconds <= 3600:
    print(f"Entered number of seconds contains:\
    \nhours: {hours:.0f}\
    \nminutes: {minutes:.0f}\
    \nseconds: {seconds:.0f}")
elif total_seconds > 3600 and total_seconds <= 86400:
    print(f"Entered number of seconds contains:\
    \ndays: {days:.0f}\
    \nhours: {hours:.0f}\
    \nminutes: {minutes:.0f}\
    \nseconds: {seconds:.0f}")
elif total_seconds > 86400:
    print(f"Entered number of seconds contains:\
    \nyears: {years:.0f}\
    \ndays: {days:.0f}\
    \nhours: {hours:.0f}\
    \nminutes: {minutes:.0f}\
    \nseconds: {seconds:.0f}")
