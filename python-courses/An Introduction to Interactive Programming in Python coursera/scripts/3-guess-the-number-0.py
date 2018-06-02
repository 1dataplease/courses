#0. import modules
import simpleguitk as simplegui
import random
import math

#1. globals - state
#rules of game - can only guess > 0 & <= 100
num_range = 100
guesses_left = 7

#2. helper fxns to initialize game
def new_game(max_range):
    global guesses_left
    print "New game. Range is from 0 to ", max_range, "\n"
    print "Number of remaining guesses is ", guesses_left, "\n"
    answer = random.randrange(1,100)

#3. classes

#4. define event handlers
# the fxns the buttons do
def range100():
    new_game(100)
       
    
def range1000():
    new_game(1000)
    
def get_input():
    global guesses_left, answer
    try:
        guess = float(input)
        if guesses_left == 0:
            print "You lose! Play again?"
        if guess > answer:
            guesses_left = guesses_left - 1
            print "Number of remaining guesses is ", guesses_left, "\n"
            print "Lower!"
        if guess < answer:
            guesses_left = guesses_left - 1
            print "Number of remaining guesses is ", guesses_left, "\n"
            print "Higher!"
        if guess == answer:
            print "You win!"
            guesses_left = 7
    except:
        print "put in a number, buddy"

#5. create a frame or window
f = simplegui.create_frame("Guess the number", 300, 300)

#6. register event handlers
#point the buttons to the fxns

f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input , 200)

#default is 0-100 game
new_game(100)

#7. start frame + timers

