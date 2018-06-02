import turtle
import math


window = turtle.Screen()
# create window(color=blue)
window.bgcolor("blue")
# create turtle(name=bob, shape=turtle, color=green, speed=9)
bob = turtle.Turtle()
bob.color("green")
bob.speed(9)
bob.shape("turtle")

#doesnt work
def koch(t, order, size):
    """
    t is the name of the turtle.
    order is the number of -^- shapes.
    size is the length of each line.
    leave turtle facing same direction
    """
    if order == 0:
        bob.forward(size)
    else:
        for angle in [60,-120,60,0]:
            koch(t, order-1, size/3)
            t.left(angle)


def f(length, depth):
    if depth == 0:
        bob.forward(length)
    else:
        f(length/3, depth-1)
        right(60)
        f(length/3, depth-1)
        left(120)
        f(length/3, depth-1)
        right(60)
        f(length/3, depth-1)

f(500,4)
