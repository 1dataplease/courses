#0. import modules
#1. globals - state
#2. helper fxns
#3. classes
#4. define event handlers
#5. create a frame
#6. register event handlers
#7. start frame + timers


#0. import modules
import simplegui

#1. globals - state
counter = 0

#2. helper fxns
def increment():
    global counter
    counter =+ 1

#3. classes
#4. define event handlers
def tick():
    increment()
    print counter

def buttonpress():
    global counter
    counter = 0

#5. create a frame
frame = simplegui.create_frame("Test", 100, 100)

#6. register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button('Click me', buttonpress)

#7. start frame + timers
frame.start()
timer.start()