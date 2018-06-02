#0. import modules
import simpleguitk as simplegui

#1. define beginning value
value = 3.12

#2. helper with single dollar or cent
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result

#  function for converting $ -> words
        
def convert(val):
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))
    
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")
    
    if dollars == 0 and cents == 0:
        return "Broke"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string

# define canvas and input handler
def draw(canvas):
#    global value
    canvas.draw_text(convert(value), (60,110), 24,  'White')

def input_handler(text):
    global value
    value = float(text)

#5. create a frame
frame = simplegui.create_frame("Converter", 300, 300)

##6. register event handlers
#frame.add_button("convert",convert,100)
frame.set_draw_handler(draw)
frame.add_input('Enter value', input_handler, 100)

#7. start frame + timers
frame.start()

# tests
print convert(11.25)
print convert(11.20)
print convert(1.25)
print convert(11.01)
print convert(0.25)
print convert(11.00)
print convert(1.01)