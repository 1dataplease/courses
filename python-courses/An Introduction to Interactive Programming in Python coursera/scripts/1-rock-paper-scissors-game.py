# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'invalid action'

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 6.5
    
def rpsls(name):
    player_number = name_to_number(name)
    # converts name/move to player_number
    
    import random
    comp_number = random.randrange(0,5)
    # compute random guess for comp_number using random.randrange()

    result = (player_number - comp_number) % 5


    print 'Player chooses', number_to_name(player_number)
    print 'Computer chooses', number_to_name(comp_number)
    
    
    if result == 0:
        print "It's a tie! Play again!'"
    elif (result == 1) or (result == 2):
        print 'Player wins!'
    elif (result == 3) or (result==4):
        print 'Computer wins!'
    else:
        print 'Please play again'

#rpsls("shoe")
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")
