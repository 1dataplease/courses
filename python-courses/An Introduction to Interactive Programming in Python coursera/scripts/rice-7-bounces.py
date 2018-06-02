#position = velocity*time
# ball motion
import simpleguitk as simplegui

# initialize globals
width = 600
height = 400
ball_radius = 20

ball_pos = [width/2, height/2]
v = [4, 5/60] # 0 x pixels / tick, 3 y pixels / tick


# event handlers    
def draw(canvas):
    # update ball position
    ball_pos[0] = ball_pos[0] + v[0]
    ball_pos[1] = ball_pos[1] + v[1]
    
    # ollide of of left canvas
    if ball_pos[0] <= ball_radius:
        v[0] = -v[0]
    #right
    if ball_pos[0] >= (width-ball_radius):
        v[0] = -v[0]

    
    
    # draw ball
    canvas.draw_circle(ball_pos, ball_radius, 2, "Red", "White")
    
# create frame
frame = simplegui.create_frame("Motion", width, height)

# register handlers
frame.set_draw_handler(draw)

frame.start()

#p(t+1) = p(0) + (t+1)v
#p(t+1) = p(t) + (1)(v(t))
