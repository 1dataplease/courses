import turtle
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    # Creates brad - he draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    i = 0    
    for i in range(4):
        brad.forward(100)
        brad.right(90)
        i = i + 1 
    # Creates angie - she draws a circle
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")
    angie.speed(3)
    angie.circle(100)
    # Creates dick - he draws a triangle
    dick = turtle.Turtle()
    dick.shape("turtle")
    dick.color("green")
    dick.speed(3)
    for i in range(3):
        dick.forward(100)
        dick.left(120)
        i = i + 1 
           
    window.exitonclick()
    
draw_shapes()

#notes
#class is a blueprint
# has info like height, rooms - can build multiple instances or objects - turtles
# webbrowser.open() is calling fxn open within webbrowser
# but turtle.Turtle() - the init() fxn within turtle that creates space
# turtle is the class, it has many fxns
