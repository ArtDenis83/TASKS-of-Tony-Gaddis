# Chapter 4. Task 16. Turtle Graphics: Repeating Squares


import turtle

t = turtle
t.speed(0)
SQUARE = 100
STEP = 5
INDENT = STEP
t.penup()
t.goto(230, -230)
t.pendown()
for counter in range(1, SQUARE, 1):
    for step in range(1, 5, 1):
        t.left(90)
        t.forward(STEP)
    STEP += INDENT
t.done()
