# Task 14. Compound Interest
# Naming variables with one letter is a bad idea, but for convenience it is implemented here.
# Formila: A = P * (1 + r / n) ** (n * t)
# A - is the amount of money in the account after the specified number of years
# Р - is the principal amount that was originally deposited into the account,
# r - is the annual interest rate.
# n - is the number of times per year that the interest is compounded,
# t - is the specified number of years.

# Get data from user
p = float(input("Enter the principal amount that was originally deposited into the account: "))
r_inp = float(input("Enter the annual interest rate: "))
n = float(input("Enter the number of times per year that the interest is compounded:"))
t = float(input("Enter specified number of years:"))

# Calculate
r = r_inp / 100
a = p * (1 + r / n) ** (n * t)

# Return result
print(f"Amount of money that will be in the account after the specified number of years: $ {a:.2f}")