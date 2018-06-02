#0. import modules
import simpleguitk as simplegui
import random

#1. globals - state
message = 'heyo' #"you wanna jam. so welcome to the slam"
position = [50,50]
width = 500
height = 500
interval = 2000

#4. define handler for text box - updating screensaver msg
def update_msg(text):
    global message
    message = text

# define handler for timer
def new_position():
    global position
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y

# def handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 26, "Red")

#5. create a frame
frame = simplegui.create_frame('Home', width, height)


#6. register event handlers
text = frame.add_input("Message:", update_msg, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, new_position) #time_in_ms, fxn

#7. start timer first, then frame
timer.start()
frame.start()

