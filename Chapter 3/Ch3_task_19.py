# Task 19. Turtle Graphics: Hit the Target Modification
# Not complete, it is necessary to remove the requirement "change angle" when hit

import turtle

# Set constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_Х = 100  # lower left X coordinate of the target.
TARGET_LLEFT_Y = 250  # lower left Y coordinate of the target.
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1  # Animation speed of the projectile
NORTH = 90  # North direction angle.
SOUTH = 270  # South direction angle.
EAST = 0  # East direction angle.
WEST = 180  # West direction angle.

# Draw a window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

#  Draw a target.
turtle.hideturtle()
turtle.speed()
turtle.penup()
turtle.goto(TARGET_LLEFT_Х, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get angle and force frim user.
angle = float(input("Enter pointing angle: "))
force = float(input("Enter force value (1-10): "))

# Calculation distance.
distance = force * FORCE_FACTOR

# Set the direction.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Calculation of target hit
if (turtle.xcor() >= TARGET_LLEFT_Х and
    turtle.xcor() <= (TARGET_LLEFT_Х + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Target hit!')
else:
    print('You missed')
if (turtle.xcor() >= TARGET_LLEFT_Х and turtle.ycor() >= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Use less force')
elif (turtle.xcor() >= (TARGET_LLEFT_Х + TARGET_WIDTH) and turtle.ycor() >= TARGET_LLEFT_Y):
    print('Use less force')
elif (turtle.xcor() <= TARGET_LLEFT_Х and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Use more force')
elif (turtle.xcor() <= (TARGET_LLEFT_Х + TARGET_WIDTH) and turtle.ycor() <= TARGET_LLEFT_Y):
    print('Use more force')
else:
    print("Change angle")

turtle.done()