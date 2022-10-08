# Chapter 4. Task 18. Turtle Graphics: Hypnotic Pattern


import turtle

t = turtle
t.speed(0)
ITERATIONS = 10
LENGTH = 25
STEP = LENGTH
for counter in range(0, ITERATIONS, 1):
    for sqare in range(1, 3, 1):
        t.left(90)
        t.forward(LENGTH)
    LENGTH += STEP
t.done()
