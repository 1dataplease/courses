#position = velocity*time
# ball motion
import simpleguitk as simplegui

# initialize globals
width = 600
height = 400
ball_radius = 20

initial_pos = [width/2, height/2]
velocity = [0,3] # 0 x pixels / tick, 3 y pixels / tick
time = 0

# event handlers
def tick():
    global time
    time = time+1
    
def draw(canvas):
    # create list to hold ball position
    ball_pos = [0, 0]
    
    # calculate ball position
    ball_pos[0] = initial_pos[0] + time * velocity[0]
    ball_pos[1] = initial_pos[1] + time * velocity[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, ball_radius, 2, "Red", "White")
    
# create frame
frame = simplegui.create_frame("Motion", width, height)

# register handlers
frame.set_draw_handler(draw)
timer1 = simplegui.create_timer(100, tick)

timer1.start()
frame.start()

#p(t+1) = p(0) + (t+1)v
#p(t+1) = p(t) + (1)(v(t))
