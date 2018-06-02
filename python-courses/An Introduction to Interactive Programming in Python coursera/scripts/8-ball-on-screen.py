import simpleguitk as simplegui

# initialize globals
width = 600
height = 400
ball_radius = 20

ball_pos = [width/2, height/2]
vel = [-40/60, 5/60]

#define event handlers
def draw(canvas):
    canvas.draw_circle(ball_pos, ball_radius, 2, "Red", "White")
    
def keydown(key):
    vel = 4 #pixels of mvmnt
    if key == simplegui.KEY_MAP['left']:
        ball_pos[0] -= vel
    elif key == simplegui.KEY_MAP['right']:
        ball_pos[0] += vel
    elif key == simplegui.KEY_MAP['down']:
        ball_pos[1] += vel
    elif key == simplegui.KEY_MAP['up']:
        ball_pos[1] -= vel

# create frame
frame = simplegui.create_frame("Ball control", width, height)

# register draw and keydown
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

#start frame
frame.start()