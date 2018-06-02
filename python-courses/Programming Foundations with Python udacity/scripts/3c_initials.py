import turtle
import math


window = turtle.Screen()
# create window(color=blue)
window.bgcolor("blue")
# create turtle(name=bob, shape=turtle, color=green, speed=9)
bob = turtle.Turtle()
bob.color("green")
bob.speed(5)
bob.shape("turtle")

def draw_TW():
    bob.right(180)
    bob.forward(90)
    bob.right(180)
    bob.forward(45)
    bob.right(90)
    bob.forward(90)
    
    bob.penup()
    bob.left(180)
    bob.forward(90)
    bob.right(90)
    bob.forward(70)
    bob.right(60)
    bob.pendown()
    
    bob.forward(100)
    bob.left(120)
    bob.forward(60)
    bob.right(120)
    bob.forward(60)
    bob.left(120)
    bob.forward(100)

    bob.penup()
    bob.goto(0,0)
    bob.right(60)
    bob.pendown()

    window.exitonclick()


draw_TW()

