# Task 17. Wi-Fi Diagnostic Tree.

# First message
print("Reboot the computer and try to connect.")

# Get user data and return result
a = input("Did that fix the problem? yes/no: ")
if a == "yes":
	print("Thank you for contacting the support service")
else:
	print("Reboot the router and try to connect")
	a = input("Did that fix the problem? yes/no: ")
	if a == "yes":
		print("Thank you for contacting the support service")
	else:
		print("Make sure the cables between the router and modem are plugged in firmly")
		a = input("Did that fix the problem? yes/no: ")
		if a == "yes":
			print("Thank you for contacting the support service")
		else:
			print("Move the router to a new location")
			a = input("Did that fix the problem? yes/no: ")
			if a == "yes":
				print("Thank you for contacting the support service")
			else:
				print("Get a new router\nThank you for contacting the support service")