# input will come from buttons and an input field
# all output for the game will be printed in the console

# step 0 - import modules necessary
import math
import random
import simplegui

#step 1 - choose / initalize global variables for game
secret_number = 0    #int(input('Please enter a secret number: '))
allowed_range = 100
maximum_guesses = 7
guess_count = 0

#steps 2-3 define helper fxns (no classes to def) 

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global guess_count
    secret_number = random.randrange(0,100) #change later
    determine_maximum_guesses()
    guess_count = 0

def determine_maximum_guesses():
    global maximum_guesses
    maximum_guesses = math.log((allowed_range - 1), 2)
    maximum_guesses = int(math.ceil(maximum_guesses))
    return

def is_it_over():
    global guess_count
    guess_count += 1
    print "You have made", guess_count,"out of", maximum_guesses, "guesses"
    if guess_count >= maximum_guesses:
        print "You lose. The secret number was", secret_number
        print "Let's play again."
        new_game()
    else:
        print "You have", maximum_guesses-guess_count, "guesses left.\n"
    
# step 4 - define event handlers for control panel
def range100():
    global allowed_range
    secret_number = random.randrange(0,100)
    allowed_range = 100
    print "A new secret number has been chosen."
    new_game()
    

def range1000():
    #changes the range to [0,1000) and starts a new game     
    global allowed_range
    secret_number = random.randrange(0,1000)
    allowed_range = 1000
    print "A new secret number has been chosen."
    new_game()
    
def input_guess(guess):
    guess = int(guess)
    print "Guess was", guess
    if guess < secret_number:
        print "Higher"
        is_it_over()
    elif guess > secret_number:
        print "Lower"
        is_it_over()
    else:
        print "Correct!"
        new_game()

#step 5 - create frame
f = simplegui.create_frame('Game', 200, 200)

#step 6 - register event handlers
# register event handlers for control elements
r100 = f.add_button("Range: [0, 100)", range100, 200)
r1000 = f.add_button("Range: [0, 1000)", range1000, 200)

gs_inp = f.add_input("Enter a guess", input_guess, 200)


#step 7 - start frame
# call new_game 
new_game()
