# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:13:36 2017

@author: wainman
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import sys

#1-1
#optimization models, statistical models, simulation models

#1st part of model - 
#an objective fxn that can be maximized or minimized
#ex. minimize time or maximize value

#2nd part - set of constraints (possibly empty) that must be honored
#ex cant spend more than $200

# take problem, reduce it 
#to well-known problem w pre-existing solution method

#ex. knapsack problem
# finite capacity - have to decide which ones to take
#part1 - maximize value fxn
#part2- max weight you can carry

#0/1 knapsack problem - whole thing
# continuous or fractional knapsack problem

#can be computationally challenging / complex - run a long time
# because of that we dont solve, we approximate them
# use greedy algorithm to find 'good enough' solution

#formalize it:
# each item is represented by pair: (value, weight)
# cannot exceed items w cumulative weight w
# vector L, of length n, is the set of available items
# vector V, of length n, is used to indicate whether item taken
# if v[i] = 1, item I[i] is taken.

# find a V that maximizes sum (v[i] * I[i].value)      
# if we dont take it, V[i] = 0, dont care about value then

#subject to constraint that 
# sum( V[i] * I[i].weight) <= w

#1 solution - brute force algorithm
#1 enumerate every subset of items we could take - Power Set
#2 - remove all combos that exceed max weight
#3 from remaining, choose any one whose value is largest

#this is not practical, power set is massive
# V of length n. set of possible vectors = set^set
# power set is 2^n. exponential

#later, can do truly optimal solns that work almost always


#1-2
# try approx solution or exact solution that is often fast

#2 solution: greedy algo
#while knapsack not full:
#    put "best" available item in knapsack

# define best:
    #most valuable? least expensive? highest value/weight?
    # can test each of these 3 methods
    
#ex. calories reduction - max flavor w 1500 calorie restraint

#given menu of 8 items with value and colories

class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    # this one seems most useful - value/cost
    def density(self):
        return self.getValue()/self.getCost()
    
    # this just prints it out each time
    def __str__(self):
        return '{0}: <{1}, {2}>'.format(self.name,
                self.value, self.calories)

#make 3 lists - names, values, calories of each item on menu
def buildMenu(names, values, calories):
    '''3 inputs- names, values, calories lists of same length.
    name is a list of strings
    values and calories are lists of numbers
    returns a list of Foods [[apple, 20], [cheeze,val,cal]...]
    '''
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

# flexible greedy algo. flexible because of keyFunction arg
# independent of definition of best

# keyFxn has to define an ordering of the items
# we sort the items w/ sorted (fxn that returns a list)
# dont want to change the menu list argument
# we want to make a copy of menu, it will be in an order
# best to worst (reversing it)
# use key function to decide biggest/smallest
# essentially a fxn for deciding best-> worst

#then we iterate over menuCopy
# if totalCost + menuCopy.getCost <= maxCost
# add it to our resultList
# add Cost, add Value
# eventually it will stop and return resultList and Value
def greedy(menu, budgetConstraint, keyFunction):
    '''Assumes menu is a list of lists w/ val and cost, 
    budgetConstraint >= 0,
    keyFxn maps elements of menu to numbers (?)
    
    Returns a tuple of 2 items
    list sack containing elements of menu
    and totalValue, a number'''
    # use sorted to take menu, give new values, do bg->sm
    menuCopy = sorted(menu, key=keyFunction, reverse=True)
    sack = []
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(menuCopy)):
        if (totalCost + menuCopy[i].getCost()) <= budgetConstraint:
            sack.append(menuCopy[i])
            totalValue += menuCopy[i].getValue()
            totalCost += menuCopy[i].getCost()
    
    return (sack, totalValue)

# might or might not get super-optimal result
# but more efficient, addresses exponential complexity

#timing w/ n = len(menu)
# sorted = n log n
#iteration = n

# n log n + n log n = order n log n
# which is much less than 2 log n

#given list, contraint and maximizer,
# prints out the totalValue, and each item-val combo
# this is only created so that we can insert 3 keyFxns
# for cost, value and density
def testGreedy(menu, budgetConstraint, keyFunction):
    sack, val = greedy(menu, budgetConstraint, keyFunction)
    
    #just prints out the totalVal and prints all the items
    print('Total value of items taken =', val)
    for item in sack:
        print(' ', item)

# takes menu and constraint, gives 
def testGreedys(menu, budgetConstraint):
    print('Use greedy by value to allocate', budgetConstraint,
          'calories')
    
    testGreedy(menu, budgetConstraint, Food.getValue)
    print('\nUse greedy by cost to allocate', budgetConstraint,
          'calories')
    
    #using getCost wouldve sorted menu mostCost->leastCost
    # use lambda to do it to every item in menu, not a fxn
    testGreedy(menu, budgetConstraint, 
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', budgetConstraint,
          'calories')
    
    testGreedy(menu, budgetConstraint, Food.density)

#heres the menu or list of items u can get
#vars have to be named names, values, calories
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 
         'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 
          79, 50, 10, 150]
calories = [123, 154, 258, 354, 365, 
            150, 95, 195, 275]

# combines the 3, theyre in the class food w 3 properties
foods = buildMenu(names, values, calories)

#it will give 3 different answers, want to take best
testGreedys(foods, 750)

#aside - lambdas
#way to create anon fxn, no name
# lambda a1, a2, a3: expression
# returns a fxn of n arguments

#whatever u pass in, it returns
f1 = lambda x: x
f1(3)

#2 args
f2 = lambda x,y: x+y
f2(2,3)

# test if y times a number that equals x
f3 = lambda x,y: 'factor' if (x % y == 0) else 'not factor'

f3(3,4)

#so why do we get different answers?

# all greedy algos make a set of locally optimal choices
# this doesnt necessarily give globally optimal choice

# works fine if started on larger of 2 hills

#is greedy by density always a winner? depends on set+budget
testGreedys(foods, 1000)

#ez to implement, comp efficient
# doesnt ALWAYS yield best solution
# dont know how close it is to best answer


#1-3
#truly optimal solns

#brute force - all possible combos
# remove all combos whos total cost > budgetConstraint
# from them, choose any one whose value is greatest

#search tree / decision tree implementation
#tree built top-down starting with the root
# 1st element is selected from notChosen items

# if sackCost + elementCost < budgetConstraint:
#   node is constructed that reflects consequence of taking it
# is drawn to left (left child)
# also explore consequneces of not taking that item (right child)

# process is then applied recursively to non-leaf children
# at end, choose node w highest value

# beer->pizza->burger. can do left-first, depth-first enumeration
# go to bottom, then back up, show if we didnt take something

#what is the computational complexity - how much to compute
#time is based on # of nodes in tree
# num levels = num Items to choose from
# num nodes at level i is 2**i
# if n items, num nodes is 
nodes = 0
for i in range(len(values)):
    nodes += 2**i
print(nodes)

# this is expontential so optimize - dont explore parts that
# violate the budgetConstraint
# but the complexity of algo doesnt change even w that

# toConsider - the items that not yet gone thru/eliminated    
# budgetLeft - the budget can still take on

#header
#calling this recursively. so for each call, args will change
def maxVal(toConsider, budgetLeft):
    '''Assumes toConsider is a list of items,
    budgetLeft is a budgetConstraint number
    Returns a tuple of (total value number,
    solution list of items)
    '''
    # if 0 items left or budgetLeft is 0, valueAndItems is 0, empty
    if toConsider == [] or budgetLeft == 0:
        valAndItems = (0, ())
        
        # otherwise if nexts items cost > budgetLeft 
        # set valueAndItems to the most valuable future item
    elif toConsider[0].getCost() > budgetLeft:
        #maxVal gets the highest value under current budgetLeft?
        valAndItems = maxVal(toConsider[1:], budgetLeft)
    
        # otherwise go to the next item
    else:
        # nextItem takes the one now first in list of (val,budgets)
        nextItem = toConsider[0]
        
        # new pair variable shows the val and budget with nextItem
        # maxValOf(FutureItems, static (budgetLeft - CostCurrentItem))
        valWithIt, budgetWithIt = maxVal(toConsider[1:], budgetLeft - nextItem.getCost())
        
        # increase the valueWeHave by adding the val of the nextItem
        valWithIt += nextItem.getValue()
        
        #value if we dont take item. same as above except were not taking
        valWithoutIt, budgetWithoutIt = maxVal(toConsider[1:], budgetLeft)
            
        # test whether left/right branch better
        # test whether better to TAKE or NOT TAKE
        if valWithIt > valWithoutIt:
            # not sure why adding nextItem, blank
            valAndItems = (valWithIt, budgetWithIt + (nextItem, ))
        else:
            valAndItems = (valWithoutIt, budgetWithoutIt)
    return valAndItems

#this does not build the search tree
# local variable valAndItems records best sol found so far

def testMaxVal(menu, budgetConstraint, printItems = True):
    print('Use search tree to allocate', budgetConstraint, 'calories')
    val, sack = maxVal(menu, budgetConstraint)
    print('Total value of items taken =', val)
    
    if printItems:
        for item in sack:
            print('    ', item)

#had already set up 3 conditions of menu - names, values and budgetCosts
#new algo - best sol thus far
testMaxVal(foods, 1000)

#maybe dont like 3 drinks and 1 food - add a constraint on food/drink balance
#better answer, faster, 2^8 is not a large number, if had >8 items, could be slo


#1-4
# create a large random menu
#import random

#same as buildMenu except it creates a random benefit and cost
def buildLargeMenu(numItems, maxBenefit, maxCost):
    items = []
    for i in range(numItems):
        #food(str(i)) means it just gets the names 0,1,2,etc
        items.append(Food(str(i),
                          random.randint(1, maxBenefit),
                          random.randint(1, maxCost)))
    return items

##this builds a menu of each of these sizes
##maxBenefit of an item in each of these menus is 90, maxCost 250
#for numItems in (5,10,15,20,25,30,35,40,45):
#    items = buildLargeMenu(numItems, 90, 250)
#    #it gets pretty slow at 40 items !!!!!!!!!!!!!!!!!!!!!!!!!
#    testMaxVal(items, 750, False)

#exponentially slowing down - hopeless in theory but not in practice cuz of below

#dynamic programming - made up name to sound important/good

#recursive implementation of fibonnaci
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

##would take forever
#fib(120) is 8 sextillion, 250,000 years to finish
#fib gets slow at 32
    
#growth is proportional to growth of value of result
#problem is the number of times fib calls itself
#fib(6) = 13 = 26 calls
# a lot of same work repeatedly

#memoization
# 'trade time for space'
#create a table to record what we've done
#  before computing fib(x), check if value of fib(x) is already in the table
#    if so, look it up
#    if not, compute it, add it to the table

# memoized implementation of fibonnaco computation

#first time you call it, memo takes default value of empty dictionary
#it updates itself
def fastFib(n, memoDictOfNValPair={}):
    '''Assumes n is an int >= 0,
    memo used only by recursive calls - is a dict of n-value pairs.
    Returns fibonacci of n'''
    # this fxn can be recursive because theres a base case
    if n == 0 or n == 1:
        return 1
    
    #otherwise try to return the val for 120 inside the dict
    # 120 wont be there, it runs 119 + 118, doesnt work until 0,1
    # starts storing results from 0,1,up
    try:
        return memoDictOfNValPair[n]
    
    # has to keep running all the way from n down to 1
    # then at 1, it starts building 1,2,3, tries until 120, then top works
    except KeyError:
        # result is lastfib(current memo-dict) + 2fibsago(current memo-dict)
        result = fastFib(n-1, memoDictOfNValPair) + fastFib(n-2, memoDictOfNValPair)
        
        # now val for memo[n] gets updated, 0,1,... 120
        memoDictOfNValPair[n] = result
        return result
    
#so now run the fib for all values in between 1-120
for i in range(121):
    print('fib(' + str(i) + ') =', fastFib(i))

#much much faster

#when will memoization Dictionary or dynamic programming work?
# when theres a

#optimal substructure - when a globally optimal solution can be found by
#   combining optimal solutions to local subproblems
#       for x>1, fib(x) = fib(x-1) + fib(x-2)
# merge-sort is similar

# overlapping subproblems
#   can find an optimal soln by solving same problem multiple times
#       compute fib(x) many times 
# merge-sort doesnt have this (diff lists each time)

#0/1 knapsack problem?


#1 - 5
# yes w change

#optimal substructure
#each parent node combines a solution reached by children
#to derive an optimal soln for subtree rooted in parent
#right answer at top is the better of 2 answers below it - every time

#overlapping subproblems
# each node solves diff problem. no 2 nodes have same sack and 2 foodItems

# could run on it, but wouldnt speed it up at all

# different menu structure could give it overlapping subproblems

# a,b,c,d - val of 6,7,8,9 - calories of 3,3,2,5
# node 0: {} taken, [a,b,c,d] left, 0value, 5caloriesTilBudget

# each node is solving the problem:
    # given remaining weight, maximize value by choosing amoung itemsLeft
# budgetLeft depends on totalWeight of items taken,
#       not on which items taken or on valOfItemsTaken

# now are there overlapping subproblems
# even tho different item taken, still considering item c+d, 2 lbs left

# take maxVal, then add memo as a 3rd argument

# key of memo is a tuple: (toConsider, budgetLeft)
# num of items can be shown by len(toConsider)
# items are taken from front of list

# 1st thing body of fxn does is to check if optimal choice of items 
#  (given the budgetLeft) is already in the memo

# last thing body of fxn does is update the memo

def fastMaxVal(toConsider, budgetLeft, memo = {}):
    '''Assumes toConsider is a list of items.
    budgetLeft is a weight/cost.
    Memo supplied by recursive calls.
    Returns a tuple of the 
    (totalValofSolToTheKnapsackProblem, list of items taken)
    '''
    # this is what gets called at very end after we added it to memo
    if (len(toConsider), budgetLeft) in memo:
        valAndItems = memo[ (len(toConsider), budgetLeft)]
        
    # this is base case?
    elif toConsider == [] or budgetLeft == 0:
        valAndItems = (0, {})
    
    # if nextItem's cost > budget left
    # skip it, re-run this fxn with the item after this one
    elif toConsider[0].getCost() > budgetLeft:
        #explore not taking it / right branch only
        valAndItems = fastMaxVal(toConsider[1:], budgetLeft, memo)
    
    else:
        nextItem = toConsider[0]
        
        # explore left branch / taking item
        # go all the way thru every possible branch as if we took this one
        # find maxValOf(FutureItems, static (budgetLeft - CostCurrentItem))
        valWithIt, budgetWithIt = \
            fastMaxVal(toConsider[1:], budgetLeft - nextItem.getCost(), memo)

        #explore right branch / not taking item - all branches below
        valWithoutIt, budgetWithoutIt = \
            fastMaxVal(toConsider[1:], budgetLeft, memo)
            
        #choose to take or not to take it. choose better b/w 2 branches
        if valWithIt > valWithoutIt:
            valAndItems = (valWithIt, budgetWithIt + (nextItem, ))
        else:
            valAndItems = (valWithoutIt, budgetWithoutIt)

    #memo has key (toConsider gets longer, budgetLeft down) = (val, itemsdict)
    memo[(len(toConsider), budgetLeft)] = valAndItems
    return valAndItems

def testMaxVal2(foods, budgetConstraint, algo, printItems=True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', budgetConstraint, 'calories')
    val, sack = algo(foods, budgetConstraint)
    
    if printItems:
        print('Total value of items taken =', val)
        for item in sack:
            print('    ', item)

# do same as before, call testMaxVal and testMaxVal2 for range of items
# set maxpossibleItemVal and budgetConstraint
for numItems in (5,10,15,20,25,30,35,40,45,50, 512):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal2(items, 750, fastMaxVal, False)

#search tree wins up until 1000
#import sys
sys.getrecursionlimit()
sys.setrecursionlimit(2000)

# can do menu w size 1024 faster than a menu size 35 without dynamic prog

# fastMaxVal time ~ num of distinct (toConsider, budgetLeft) pairs
#   toConsider bounded by len(items)
#   budgetLeft is bounded by distinct sums of weights

# this is a psuedo-polynomial algo
#   at worst case, when theres not overlapping subproblems, exponential time

# greedy algos have adequate not optimal solns
# finding optimal soln is usually exponentially slow/hard

# dynamic programming yields good performance for 

#optimatization problems w optimal substructure and overlapping subproblems
# always correct, can be fast


# 1 - 6 - lecture 3
# use comp to model and solve real-world problems
#graph theory

#

















