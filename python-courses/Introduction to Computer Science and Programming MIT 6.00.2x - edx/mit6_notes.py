##2-1
#loops, str, guess-n-check, approximation, bisection

#review of loops from 1
#compute the sqroot of a num

ans = 0
neg_flag = False
x = int(input('enter an int: '))
if x < 0:
    neg_flag = True
# keep adding 1 to ans until ans^2 >= x the user put in
# guess and check - generate values for ans
# either done or gone too far
while ans**2 < x:
    #the test that depends on changing var
    ans = ans + 1
if ans**2 == x:
    print('square root of %d is %d') %(x, ans)
else:
    print(x, 'is not a perfect square')
    if neg_flag:
        print('just checking, did you mean', -x, '?')

#strings are immutable

#cheer thru all letters in word
def cheer():
    an_letters = 'aefhilmnorsxAEFHILMNORSX'
    word = input('will cheer this word: ')
    times = int(input('enthusiasm level(1-10): '))
    i = 0
    
    while i < len(word):
        char = word[i]
        if char in an_letters:
            print('give me an %s! %s' %char, char)
        else:
            print('give me a %s! %s' %char, char)
        i += 1
    print('what does that spell?')
    for i in range(times):
        print(word, '!!!')


#2-2
#approximate answer - guess close enough

#guess-n-check is exhaustive, with integer, finite #

#find sqrt or cube-root of any non-neg num, floats
# abs(guess**3) - cube <= small num epsilon

def cube_root():
    cube = 27
    epsilon = .01
    guess = .0
    increment = .0001
    num_guesses = 0
    
    #
    while abs(guess**3 - cube) >= epsilon:
        guess += increment
        num_guesses += 1
    #print once done with guesses, increments
    print('num_guesses = ', num_guesses)
    
    #if diff b/w guess and truth is larger than small num
    if abs(guess**3 - cube) >= epsilon and guess <= cube:
        print('failed on cube root of', cube)
    else:
        print(guess, 'is close to the cube root of', cube)

#if increment=.01, it went past cube_root, still run
#to fix, make sure guess<= cube in loop setup
#test capture all cases

#2-3
#bisection search
#throw away 1/2 values

#works on problems w/ ordering property
# the answer increases as the input increases
#fxn is g**2, which grows as g grows

#instead of exhaustively trying 1, 1.01
# pick a number in the middle
# if not close, ask if guess is too big or too small
# if g**2 > x: throw away >g
# if g**2 < x; throw away <g

def sqrt_bisection(num, epsilon):
    numGuesses = 0
    low = 1.0
    high = num
    #fxns guess at the sqrt
    guess = (high+low)/2.0

    # if guess^2 is - num by more than epsilon, not close
    while abs(guess**2 - num) >= epsilon:
        # print the first lo/hi/guess, guesses made below
        print('low =', str(low), 'high =', str(high), \
              'guess =', str(guess))
        numGuesses += 1
        
        # after guess, if guess too small, set low = guess
        if guess**2 < num:
            low = guess
        # if too large, set hi = hi+low/2
        else:
            high = guess
        #after the above step in guess process, make guess at mid
        guess = (high + low)/2.0

    #at end once close enough, say #guesses, fin answer, input
    print('numGuesses = ', str(numGuesses))
    print(str(guess), 'is close to sqrt of', str(num))

#strt w num n range of possible answers
#guess 1 - n/2 range
#guess 2 - n/4 range
# gth guess - n/2**g
#guess converges on order of log2N steps

#challenges - modify to work w/ negative cubes
#               modify to work with x < 1

# if x < 1
# above codes search space is 0 to x
#real answer sqrt or cube is b/w 1 and x
 #change search space to depend on value of x


##2-4
#dealing w/ floats

#why get 3.0000000005 instead of 3.0
#how do floats approximate real nums w/o storing all nums

# decimal num:
#302 = 3*10^2 + 0*10^1 + 2*10^0  
#302 = 300    +   0    +   2

# binary nums - how computer stores things - power of 2
#10011 =  1* 2^4 + 0* 2*3 + 0* 2^2 + 1 *2^1 + 1* 2^0
#          16    +   0   +    0   +   2    +  1  = 19

#how to convert decimal integer into a binary num
#last binary bit: 19%2 == 1
# 2nd to last:
# 1 + (19/2)

def intgr_to_binary(intgr):
    if intgr < 0:
        isNeg = True
        #only then we have to take the abs value
        intgr = abs(intgr)
    else:
        isNeg = False
    result = ''
    # if put in 0, just return 0
    if intgr == 0:
        result = '0'
    # as long as pos, take rema
    # 
    while intgr > 0:
        # result starts as ''
        # start from back - 1 or 0 depending on odd/even
        # 1st bit is 1 (since 19)
        # divide 19//2 -> 9
        # 2nd bit is 1
        # then take original int 9//2 = new int 4
        # 3rd bit is 0, since 4 is even
        # 4-> 2, 
        # 4th bit is 0
        # 2-> 1
        # 5th bit is 1
        # 10011
        result = str(intgr%2) + result
        intgr = intgr // 2
    if isNeg:
        result = '-' + result
    return result

#fractions to binary
# 3/8 = .375 = 3* 10^-1 + 7* 10^-2 + 5* 10^-3  

# multiply it by large enough number to get an int
# turn that int to binary
# then divide by that large number
# that large number has to be a power of 2 - 2 4 8 16

#.375 * 8 = 3
#bit1: 1
#3//2 = 1
#1 is odd
#bit2: 1
#11 divide by 2**3 means shifting right 3 spots
#.011

def decimal_to_binary(decimal):
    #will loop thru powers 2^0, 2^1, 1 2 4 8 16 multiplier
    decimal = float(decimal)
    power = 0
    # keep going 1 2 4 until dec*power is an odd intgr
    while ((2**power)*decimal) % 1 != 0:
        print('remainder = ', str((2**power) *decimal \
              - int((2**power) * decimal)))
        power += 1
    
    # now that have correct power, intgr is dec * 2^power
    intgr = int((2**power) * decimal)
    
    #set result blank, add bits
    result = ''
    if intgr == 0:
        result = '0'
    # the intgr steps for adding bits to result
    while intgr > 0:
        result = str(intgr%2) + result
        intgr = intgr//2
    # move the decimal to the right # of spaces of the power
    for i in range(power - len(result)):
        result = '0' + result
    # all but last few binary digits, . the binary digits
    result = result[0:-power] + '.' + result[-power:]
    print('The binary representation of the decimal', str(decimal),\
          'is', result)
#.333 is very way too long, gets close but not perfect number

#if no intgr 'power' such that decimal* 2**power is an intgr
# then internal representation is always an approximation

# so dont ask if 3.5425 == 3.54250
# binary representation might be really close instead of exact
# to test equality, better off asking if
# abs(3.54250 - 3.5425) < .001

# why does print .1 return .1 if not exact
# python set it up so it automatically rounds to the closest flt


#2-5
#newton-raphson
# general approx algorithm to find roots of a polynomial in 1 var










#numbers, assignments, input/output, comparisons, loops
#turing complete - anything thats computable can be computed

#but the code lacks abstraction - have to reload file, change parameters
# cant use same variable names elsewhere in code

# fxn gives us abstraction - lets us capture computation
# and treat as if a primative (something given to us by py we can use)

##ex - want z to be the max of x and y
#if x>y:
#    z=x
#else:
#    z=y
    
#but we would have to copy it everywhere we want to use
# also cant reuse x and y

#wrap up recipe - use by calling name and providing input
# internal details hidden from users - a black box

# def <fxnname>(<formal parameters>):
#    <fxn body>

# within parenthesis are 0 or more formal parameters
#   each is a variable name to be used inside fxn body

def max(x,y):
    if x>y:
        return x
    else:
        return y

# invoke or call this function
z = max(3,4)
# x is bound to 3, y to 4, body expression evaluated

#body can consist of any # of legal py expressions
# expressions evaluated until run out (body bottom)
#or if nothing returned None returned

#expressions for each parameter evaluated, bound to parameter names of fxn
# control transfers to 1st expression in body of fxn
# body expressions executed until return or run out (then return=None)
# invocation is bound to the returned value

#L4-5
#local bindings diff from global bindings
def square(x):
    return x*x
  
#2 to the power of n. keeps squaring until n=1  
def twoPower(x,n):
    while n>1:
        x=square(x)
        n=n/2
    return x
#(2,8)
#2.4.16, 256
#8,4,2,1
    
#fxn procedure creates new frame
    #new x and n are binded locally
    # while n>1, T
    # if theres no local square, can find it from global
    # x now bound to 4, the square frame goes away
    # take n rebound to 4
    # n still > 1
    # get square fxn, create frame, its bound to 4, now 16, delete frame
    # x locally now 16, n/2 now 2

#each call to each procedure creates its own frame
# it inherits from env where procedure said it should
# locally still keeping track of it


#L4-7
# useful to group fxns together that share a common theme
# can put them into a single .py file
# we can import those computations

# 5 functions into circle.py
#whether in a python shell or in another file
#circle.pi instead of my wrong local pi value
# from the context circle, import area fxn
# lets us create files with commonality

#can also just say from circle import *
#will still get the area (and dont need to say circle.area)
# can make overriding changes, otherwises uses the imports expressions


#L5-1
#fxn can come in different types

#iterative algorithms
#looping constructions - while or foor loop
# capturing computation in set of 'state variables' which
#   update or change their values on each time thru loop

#if we wanted to do multiplication by successive additions
#to a*b, add a+itself b times

#state variables:
#   i - iteration number, it starts at b
#   result - current value of computation, starts at 0

#update rules:
# i <- i-1; stop when at 0
# result <- result+a

def iterMult(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
    
# initialize 1 state variable - result = 0
# use parameter b as other state variable = iteration number
 
   
#L5-2

#resurive algorithms
# computation as a*b = a + a + ... + a (there are b copies of a)
# same as doing a + (b-1) copies of a
#               a + a*(b-1)

# reduced it to a simple operation a, and simpler execution
# taken problem, reduce it to simpler/easier version

#how can we reduce this to simpler/smaller version of same plus simple comps
# reduce until a simple case - base case
# a*b = a; if b=1
# a*b = a + a*(b-1); otherwise (recursive case)

def recurMult(a,b):
    if b==1:
        return a
    else:
        return a + recurMult(a,b-1)
        
#keep doing the same bottom fxn until otherwise case, do easy return

# given 2 values, check if b==1
# if it is, just return a

# otherwise, call same function w/ simpler argument
# do it again except with a + FXN(a,b-1)

#L5-3
#how does it know which values of variables to use
#calling it creates new environment, inherits 1st frame
# get values of 2 inputs a=3,b=2
# b!=1 so else clause
#   2 + 
#   create new frame so a=2, b=2
#   2 +
#   now b->1
#   b==1 so 2
# = 6

# 1. each recursive call to a fxn creates its own encironment
#   local scoping of variables
# 2. bindings for variables in each frame are distinct
#   not changed by recursive call
# 3. flow of control can pass to earlier frame once fxn call
#   returns its value


#L5-4
#how do we know it will stop and compute our value

#itermult stops because b is +, decreases by 1, eventually 0

#recurMult called w/ b=1 has no recursive call and stops, correct

# if we call recurMult w/ b>1, makes one with smaller
# until eventually b=1

# math induction
# to prove a statement where 1 of parameters is an integer
    # if we want to show its true for all values of n

#1.  prove its true when n is smallest value n=0 or n=1

#2. prove that its true for an arbitrary value of n
#   it must be true for n+1

#given any value, its true for next value 
#(induction tells us its true for all values of n)

#prove that
# 0 + 1 + 2 + ... + n = (n(n+1))/2

#1 look at result of base case
# if n=0, then 0 = 0*1/2 = 0, true

#2 inductive step 
#assume that its true for value k, we need to show k+1
# we assume A its true that 0+1+2+...+k = (k(k+1))/2
# need to show that 0+1+2+...+k+(k+1) = (k+1)(k+2)/2

# so on left, we have the right hand side of assume A + alg k+1
#   k(k+1)/2 + k+1
# by algebra, that becomes
#   ((k+1)(k+2)/2

# in base case, can show fxn stops, and returns a*1=a correct
#   assume recurMUL correctly returns answer for problems smaller than b
#   then by the addition step, it also returns correct answer for 
#problem size b


#L5-6.2
#ex of hard to do in iterating, better recursive

# temple in hanoi - 3 spikes
# spike 1 has 64 diff size discs
# need to move stack to second spike
# disc cant be on smaller disc

# want to move stack of size n to target
# take stack size n-1 move to empty
# move bottom one to diff spare
# move whole stack to that bottom

# take smaller size problem (n-1) stacks put them (solve it)
# solve the base case (the bottom one)
# resolve the smaller size problem (to go on top of base)

def printMove(fr, to):
    print 'move from',str(fr),'to',str(to)

def Towers(n,fr,to,spare):
    if n==1:
        printMove(fr,to) #move the 1 bottom disc from->to places
    else:
        Towers(n-1,fr,spare,to) #move a smaller stack to spare
        Towers(1,fr,to,spare)   #move the bottom to tower you want filled
        Towers(n-1,spare,to,fr) #move the smaller stack to the one you want filled

#ex
Towers(1, 'f', 't', 's')
print '\n'
Towers(2, 'f', 't', 's')
print '\n'
Towers(3, 'f', 't', 's')

#L5-7
#recursion w/ multiple base cases

#pisa/fibonacci model how rabbits breed

# 1m+1f in pen, mate at 1month, 1 month pregnancy
# assume rabbits never die, female always produces 1m+1f
#   every month from its 2nd month on

# how many females at end of 1yr/2yr/we

#month0 - 1 female
#month1 - 1 (pregnant)
#month2 - 2 (new one)
#month3 - 3 (delivered again, one preg)
#month4 - 5 (delivered, delivered)
#month5 - 8
#month6 - 13

#basically just adds up the previous 2 months

# females(n) = females(n-1) + females(n-2)
#  every female alive at month n-2 produces 1 in month n
#  these can be added to those in month n-1 
#   to get total in month n

# 2 base cases
# females(0) = 1
# females(1) = 1

# recursive case
# females(n) = females(n-1) + females(n-2)

def fib(x):
    '''assumes x an int>=0
    returns fibonacci of x'''
    assert type(x) == int and x >= 0 #takes a boolean, if F break
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

#L5-9
#global variables
        
#suppose we wanted to count # of times fib called itself
# all fxns have communicated thru fxn parameters and return values
        
# we can make a variable outside fxn
def fibMeter(x):
    global numCalls #we define this within fxn, change glob
    numCalls += 1
    if x==0 or x==1:
        return 1
    else:
        return fibMeter(x-1) + fibMeter(x-2)

#input is number being fibbed, output is fib(x) and times recursive called
def testFib(n):   
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print 'fib of', str(i), '=', str(fibMeter(i))
        print 'fib called', str(numCalls), 'times'
        
testFib(5)

#destroys locality of code - all of fxn contains whats needed in it
# can be modified/read in many places - break locality / intro bugs

#L6-1
# compound data types

# seen exhausive unmeration, guess and check, bisection, divide+conquer
# on num and strings

#tuples, lists, dictionaries

#tuples
#ordered sequence of elements (sim 2 strs)
t1 = (1, 'two', 3)

#elements can include other elements
t2 = (t1, 'four')
print t2
print t1+t2 #like concatenation

#index - go into tuple, get out element
print ((t1+t2)[3])

#singleton - have to give a comma and no element after
t3 = ('five',)
print t1+t2+t3

#iterate over tuples
def findDivisors(n1,n2):
    '''assumes n1 and n2 positive ints
    returns tuple containing
    common divisors of n1 and n2'''
    divisors = () #empty tuple
    for i in range(1, min(n1,n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            divisors = divisors + (i,)
    return divisors
print '\n', findDivisors(20,100)

divs = findDivisors(20,100)
total = 0
for d in divs:
    total+= d
print total

#L6-4
#fxns as objects
# they are 1st class objects
# can have types
# can be elements in data structures like lists, tuples, dicts
# can appear in expressions
#   as right side of assignment or as an argument to a fxn

#use fxns as arguments when coupling w/ lists
# higher order programming

#applying fxn to list of a number
def applyToEach(L, f):
    '''assume l is list, f is fxn
    mutates L by replacing each element e,
    with function on that list element f(e)'''
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1,-2, 3.3]
applyToEach(L,abs)
print L
applyToEach(L,int)
print L

#applying list of fxns to a number
#fxns can be members of lists, loop over that list
def applyFuns(L,x):
    for f in L:
        print f(x)
        
applyFuns([abs,int,fib],4)

#generalization of higher order fxn

#python provides a general purpose higher order fxn map

#simple form
# takes 1 fxn and many arguments
print map(abs,[1,2,3,-4])

#general form
# takes fxn that takes n arguments, map will apply
L1 = [1,28,36]
L2 = [2,56,9]

#runs fxn on each index of all lists
print map(min,L1,L2) 


#L6-5
#dictionary

#indices dont have to be integers, can be strings
# no longer indices but keys
# dict is collection of <key,value> pairs

#can only be acessed with the key, not the index

monthNumbers = {'jan':1, 'feb':2, 'mar':3, 
                1:'jan', 2:'feb', 3:'mar'}

##can insert a change
monthNumbers['apr'] = 4

#iter over dict
collect = {}
#for e in monthNumbers:
#    collect.append(e)

#keys method on a dict
monthNumbers.keys()

#keys must be immutable
#can have tuple in a dict, but not a list
myDict = {(1,2): 'twelve', (1,3): 'thirteen'}
myDict[(1,2)] #returns twelve

#L7-1
#test and debug
#ways of trying code on examples to see if running correct

#design code for ease of testing and debugging
#break code into peices - independently test/debug

#document constraints on modules
#expectations on inputs, outputs
#detail assumptions

#runnable, have a set of input-output pairings

#L7-2
#testing

#goal - show bugs exist, show
#formal methods on simple kinds of code

#test suite
#find collection of inputs w/ hi liklihood of showing bug
#partition space of inputs into subsets that provide
#   eqivalent info about correctness
# partition divides set into group of subsets so each element of set
#   is in exactly 1 subset

def isBigger(x,y):
    '''Assumes x and y are ints
    returns True if x less than y
    else False'''
    
#input space is all pairs of integers
#possible partition
# x + y +
# x - y - 
# x + y -
# x=0, y=0
# x=0, y -
# x=0, y+
# x +, y=0
# x -, y=0

# 2 inputs to the 3 conditions (+,-,0) gives 8 tests

#couldve chosen primes, not relevant to problem
#spaces of inputs often have natural boundaries
#integers have 3

#if no natural partition to input space

#random testing
# prob that code is correct increases w/ # trials

#blackbox testing
#use heuristics based on exploring paths thru specs

#glassbox testing
#use heuristics based on exploring paths thru the code

#L7-6

#runtime bugs
#occurs during code running

#overt bug - obvious - crash or runs forever

#covert - returns value, but in some cases may be incorrect
#   harder to detect, dangerous

#persistant bug - occurs everytime

#intermitant = can be ~input or diff outputs from same input

#defensive - if overt/persistant bug, falls in

#SPR L3-1
#iteration

#start w/ a test
# if evaluates to True, execute loop body once
#go back to reevaluate test
#repeat until test evaluates to false
#code following iteration is executed

#l3-2
#guess and check method

#declarative def of sqrt(x)
#if we could guess possible values for sqrt (called guess g)
# can use def to check if g*g=x
#just need good way to generate guesses

#finding cube root of int
#assume x is int
##try 0,1,2,3, until k**# > x
## only a finite number of cases to try

#print 'perfect cube\n'
#
#x = int(raw_input('enter an int: '))
#ans = 0
#while ans**3 < x:
#    ans = ans + 1
#if ans** 3 != x:
#    print str(x), 'is not a perfect cube'
#else:
#    print 'cube root of', str(x), 'is', str(ans)
    
#loop characteristics
#need to initialize outside loop, loop variable changes
# test for termination depends on the loop variable
    
#decrementing fxn
#when loop entered, value not negative
#when value <= 0, loop terminates
# value of decr fxn is decreased everytime thru loop
#in ex, decrementing value was abs(x) - ans**3
    
#what happens if we dont initialize the variable?
    # error: that loop variable was never defined
    
# what if we dont change variable inside loop?
    # it stays at the same value of 0, infinite loop
    # test initially true, stays true, inf loop    

#exhaustive enumeration
#guess and check can work when finite # of possibilities
#good way to generate guesses in organized manner

#L3-3
#for loop
#while loops iterate over sequence of choices (often ints)
# for identifier in sequence

#until out of choices or hit a break stmt
#range(n) = [0,1,2,3... n-1]
#range(3,7) = [3,4,5,6]

##foor loop, this time accting negatives
#x = int(raw_input('enter an int: '))
#for ans in range(0, abs(x)+1):
#    if ans** 3 != x:
#        break
#if ans**3 != abs(x):
#    print str(x), 'is not a perfect cube'
#else:
#    if x<0:
#        ans = -ans
#    print 'cube root of', str(x), 'is', str(ans)

#L3-4
#floats approx real numbers

#decimal numbers (10)
#302 = 3*10**2 + 0*10**1 + 2*10**0

#binary
#10011 = 1*2**4 + 0*2**3 + 0*2**2 + 1*2**1 + 1*2**0
#in decimel thats
#           16 +    0   +       0 + 2 +     1 = 19

#converting decimal int to binary

#1 take remained of x relative to 2
#x % 2
# that gives us the lowest order (furtherst right) bit

#2 divide x by 2
# x/2
# all the bits get shifted left
#10011 = 1*2**3 + 0*2**2 + 0*2**1 + 1*2**0 = 1001

#keep doing successive divisions, remainder gets next bit,etc

#if no int such that x*(2**p) is a whole number
#internal representation is an approximation

#implication
#testing equality of floats not exact
#abs(x-y) < .0001, rather than x==y
#print .1 returns .1 but not exact to autoround

#L3-5
#iterative / guess + check dealing with floats
#approximate solutions

#we want to find sqrt of any non-negative float number
#cant guaruntee exact, look close enough
#start with exhaustive enumeration
#   take small steps to generate guesses in order, see if close

#exhaustive enumeration

#x=25
#epsilon = .01 #how close do i want to get
#step = epsilon**2
#numGuesses=0
#ans = 0.0
#
##1 check if ans**2 - input > epsilon_error
##2 check that answer is less than x 
#while (abs(ans**2 - x)) >= epsilon and ans <= x:
#    ans += step
#    numGuesses += 1
#print 'numGuesses =', str(numGuesses)
#
#if abs(ans**2-x) >= epsilon:
#    print 'failed on square root of', str(x)
#else:
#    print str(ans), 'is close to the square root of', str(x)

#step could be any small number
#too small, length
#too large, may skip over answer without getting close enough

#L3-6
#bisection search

#know that sqrt(x) is b/w 0 and x

#exhaustive enumeration
#we said 0+lil+2lil+...

#instead, lets pick the midpoint, try it
# ask if its too big or too small

#if g**2 > x, 

#x = 25
#epsilon = .01 #once youre within, close enough
#numGuesses = 0
#low = 0.0
#high = x
#ans = (high+low)/2.0
#while abs(ans**2 - x) >= epsilon:
#    print 'low =', str(low), 'high =', str(high), 'ans =', str(ans)
#    numGuesses += 1
#    if ans**2 < x:
#        low = ans
#    else:
#        high = ans
#    ans = (high + low)/2.0
#print 'numGuesses =', str(numGuesses)
#print str(ans), 'is close to the square root of', str(x)

#1mm to 26 steps

#radically reduces computation time, smart about guesses
#should work on problems with an ordering property
#value of fxn being solved varies monotonically w/ input value
#       here, fxn is g**2, which grows as g grows

#L3-7
#newton-raphson algo

#find root of polynomial in 1 variable
#some sequence of coefficients x and powers 
# want to find the place where the graph crosses x, p(x)=0
#p(x) =  anx^n + a0

# to find sqrt of 24
#find the root of p(x) = x**2 - 24

#if g is an approx to the root, then
# g - p(g) / p'(g)
# is a better approx
#p' is derivative of p

#ex
#simple case: cx**2 + k
# first deriv:  2cx
# so if polynomial is x**2 + k , deriv is 2x

#given a guess g for the sqr root,
# a better guess is 
#   g - (g**2 - k)/2g

epsilon = .01
y = 24.0
guess = y/2.0

# y is is the number we are trying to sqroot
#check to see if guess**2 - y < epsion
# if no, new guess is guess = (guess**2 - y) / 2*guess
while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) -y)/(2*guess))
    print guess
print 'square root of', str(y), 'is about', str(guess)

#generate good guesses and test them

#terative algos
#use same code repeatedly

#guess+check
#use looping construct to generate guesses

#generating guesses
#exhaustive enumeration
#bisection search
#newton-raphson (for root checking)

#SPR 8-2

#how exceptions can help
#compute grades for a class

#given class list containing 
#list of first and last name
#and list of grade on assignments

#a class subject and list of weights
def convertLetterGrade(grade):
    if type(grade) == int:
        return grade
    elif grade == 'A':
        return 90.0
    elif grade == 'B':
        return 80.0
    elif grade == 'C':
        return 70.0
    elif grade == 'D':
        return 60.0
    else:
        return 50

def getSubjectStats(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)]
        for elt in subject]

#given 2 lists, run down them:  a[0] * b[0] + (a[1] * b[1])
def dotProduct(a,b):
    result = 0.0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result

#get dotproduct of them and divide by # of tests to get avg   
def avg(grades,weights):
    try:
        return dotProduct(grades,weights)/len(grades)
    except ZeroDivisionError:
        print 'no grades data'
        return 0.0
    except TypeError:
        newgr = [convertLetterGrade(elt) for elt in grades]
        return dotProduct(newgr, weights)/len(newgr)

#an error if no grades for a student
#now itll return a value None
# or change policy so none is 0
    
#L8-3
# exceptions to control flow thru code

# raise  exceptionName(arguments)

#traditional code
def getRatios(v1,v2):
    ratios=[]
    if len(v1) != len(v2):
        raise ValueError('bad arg')
    for index in range(len(v1)):
        v1Elt = v1[index]
        v2Elt = v2[index]
        if (type(v1Elt) not in (int, float))\
        or (type(v2Elt) not in (int,float)):
            raise ValueError('bad arg')
        if v2Elt == 0.0:
            ratios.append(float('NaN'))
        else:
            ratios.append(v1Elt/v2Elt)
    return ratios


#except clause makes it much easier
def getRatios(v1,v2):
    '''Assumes v1 and v2 are lists of equal length of nums
    Returns a list containing the meaningful values of
    v1[i]/v2[i]'''
    ratios=[]
    for index in range(len(v1)):
        try:
            ratios.append(v1[index]/float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('getRatios called with bad arg')
    return ratios
 
   
try:
    print getRatios([1.0, 2.0, 7.0, 6.0],
                    [1.0, 2.0, 0.0, 3.0])
    print getRatios([],[])
    print getRatios([1.0, 2.0], [3.0])
except ValueError, msg:
    print msg

#L8-3
#assertion

#if want 2 be sure that assumptions are as expected
#cant control response, raise AssertionError
#defensive programming

def avg(grades,weights):
    assert not len(grades) == 0, 'no grades data'
    newgr = [convertLetterGrade(elt) for elt in grades]
    return dotProduct(newgr, weights)/len(newgr)

# as long as top is true, carry on. else, stop
# error will print out 'no grades data'
#   can check inputs, use anywhere, make it easier to find bug source

# 2 preconditions, 1 post-condition
def avg(grades,weights):
    assert not len(grades) == 0, 'no grades data'
    assert len(grades) == len(weights), 'wrong num of grades'
    newgr = [convertLetterGrade(elt) for elt in grades]
    result = dotProduct(newgr, weights)/len(newgr)
    assert 0.0 <= result <= 100.0
    return result

#avoid propogating bad values
#goal is to spot bugs early, make clear where it happened
#catch at first point of contact instead of tracing back

#supplement to testing

# rely on raising exceptions if user gives bad input

# use assertions for checking
# types of arguments or values
# constraints on return values
# ex. no dups in a list

