#0. import modules
import simplegui

#1. globals - state
#2. helper fxns
#3. classes
#4. define event handlers
def draw(canvas):
    canvas.draw_text('Hello!', (100,100), 24, 'WHite')
    canvas.draw_circle((100,100), 5, 5, 'Red')

#5. create a frame
frame = simplegui.create_frame('Test', 300, 200)

#6. register event handlers
#7. start frame + timers