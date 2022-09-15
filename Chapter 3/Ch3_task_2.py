# task 2. Areas of Rectangles

# Get data from user
length1 = float(input("Enter length of rectangle1: "))
width1 = float(input("Enter width of rectangle1: "))
length2 = float(input("Enter length of rectangle2: "))
width2 = float(input("Enter width of rectangle2: "))

# Calculate
rectangle1_area = length1 * width1
rectangle2_area = length2 * width2
r1 = rectangle1_area
r2 = rectangle2_area

# Return result
if r1 == r2:
    print("The area of both rectangles is the same")
elif r1 > r2:
    print("The area of a rectangle 1 is greater than rectangle 2")
elif r1 < r2:
    print("The area of a rectangle 2 is greater than rectangle 1")
