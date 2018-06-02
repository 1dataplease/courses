#0. import modules
import simpleguitk as simplegui
import math

#1. globals - state
store = 12
operand = 3

#2. helper fxns

#3. classes

#4. define event handlers
def output():
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    global store, operand
    store,operand = operand,store
    output()

def add():
    global store, operand
    store = store + operand
    output()

def subtract():
    global store, operand
    store = store - operand
    output()

def multiply():
    global store, operand
    store = store * operand
    output()

def divide():
    global store ,operand
    store = store / operand
    output()

def sqr():
    global store, operand
    store = store**2
    output()

def sqrt():
    global store, operand
    store = math.sqrt(store)
    output()


#add the numbers on calculator
def enter(input):
    global store, operand
    operand = float(input)
    output()

#5. create a frame
frame = simplegui.create_frame("Calculator", 300, 300)

#6. register event handlers
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("+", add, 100)
frame.add_button("-", subtract, 100)
frame.add_button("/", divide, 100)
frame.add_button("*", multiply, 100)
frame.add_button("^2", sqr, 100)
frame.add_button("sqrt", sqrt, 100)
frame.add_input("Enter operand", enter, 100)

#7. start frame + timers
frame.start()