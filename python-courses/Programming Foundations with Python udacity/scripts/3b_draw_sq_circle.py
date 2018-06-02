import turtle
def draw_square_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    # Creates brad - he draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(8)

    def square():
        side = 0
        for side in range(4):
            brad.forward(100)
            brad.right(90)
            side = side + 1
    counter = 0
    turn = 10
    for deg in range(360/turn):
        square()
        brad.right(turn)
        
    window.exitonclick()

draw_square_circle()
