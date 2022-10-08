# Chapter 4. Task 19. Turtle Graphics: STOP Sign

import turtle

t = turtle
t.speed(0)
t.pensize(5)
t.penup()
t.goto(-50, -100)
t.pendown()
for counter in range(1, 9, 1):
    t.forward(100)
    t.left(45)
t.penup()
t.goto(-8, 18)
t.write("STOP")
t.done()
