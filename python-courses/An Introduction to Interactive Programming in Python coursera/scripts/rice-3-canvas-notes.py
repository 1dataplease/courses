import simpleguitk as simplegui

message = "Welcome!"

def click():
    '''Change message on mouse click'''
    global message
    message = "Good job!"
    
def draw(canvas):
    '''Draw message'''
    canvas.draw_text(message, [50,112], 22, 'Blue')
    
# create frame, assign callbacks
    
frame = simplegui.create_frame("Home", 300,300)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

#if blank, have to start it
frame.start()