import simpleguitk as simplegui

size = 10
radius = 10

# define button handlers, circle-draw handler

def increase_button_handler():
    '''increases the size'''
    global size
    if size > 0:
        size += 1
    label.set_text("Value: "+str(size))
    
def decrease_button_handler():
    '''decreases the size'''
    global size
    if size > 0:
        size -= 1
    label.set_text("Value: "+str(size))
    
def change_radius_handler():
    '''changes the circle radius'''
    global radius
    radius = size
    radiuslabel.set_text("Radius: "+str(radius))
    
def draw_handler(canvas):
    '''draws the circle'''
    canvas.draw_circle((100,100), radius, 5, "Red")
    
# create a frame, assign callbacks to event handlers
    
frame = simplegui.create_frame("Home", 200, 200)

label = frame.add_label("Value: "+str(size))
frame.add_button("Increase", increase_button_handler)
frame.add_button("Decrease", decrease_button_handler)

radiuslabel = frame.add_label("Radius: "+str(radius))
frame.add_button("Change circle", change_radius_handler)

frame.set_draw_handler(draw_handler)
frame.start()