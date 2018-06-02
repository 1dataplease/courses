# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 08:35:57 2018

@author: wainman
"""

##pg 14, 2.1 - diving in
def odbchelper():
    def buildConnectionString(params):
        '''
        Build a connection string from a dictionary of parameters
        Returns a string
        '''
        return ';'.join(['%s=%s' % (k,v) for k,v in params.items()])
    
    if __name__ == '__main__':
        myParams = {
                    'server': 'mpilgrim',
                    'database': 'master',
                    'uid': 'sa',
                    'pwd': 'secret'
                    }
        print buildConnectionString(myParams)
## this fxn takes a dictionary of strings
## prints key=value;key2=value2;etc.
## the way of testing is if __name__ == '__main__'
## then typing the variable and running program
odbchelper()
## on this machine have to run with ipython script.py
## python script.py doesnt work

### 2.2 declaring fxns
## 2.2.1 datatypes
## dynamically typed - discovered at execution time
## strongly typed - types are always enforced

## 2.6 testing modules
## module is an object
## can import dive-into-python
## get name from dive-into-python.__name__
## so the if stmt only works if running it without import

#add to path in order to import a module
import sys
sys.path
sys.path.append('/new/location')

#dictionaries
## ex 3.4 - mixing datatypes in a dict
d = {"server":"mpilgrim", "database":"master", 
     'uid': 'sa', 'retrycount': 3}
d[42] = 'douglas'

## dict keys can be strs, ints

#mutable
## del from dict
del d[42]

#3 del all items in dict
d.clear()

## 3.2.2 adding to lists
li = ['a', 'b', 'mpilgrim', 'z', 'example', 'new']
## inserts after 2nd item or into position 2
li.insert(2, 'new')

## add list2 to end of list1
#extend - conatenates list
li2 = ['two', 'elements']
li.extend(li2)

## using append would just create in that 1 position a sublist
li.append(li2)
# remove
li.pop()


## 3.2.3 searching lists
# get index by typing the value
li.index('example')
# it gets 1st one if it appears twice
li.index('new')

# remove only the 1st new
li.remove('new')

# can also extend with + sign, as long as its assigned
li = li + li2

# can get 3 of that list
li = [1,2]*3

## 3.3 tuples
# elements have a defined order like a list
t = ('a', 'b', 'mpilgrim', 'z', 'example')
t[1:3]

# cannot append, remove or index
# can find 'a' in t
'a' in t

## can assign consecutive values
## each of these variable names will have vals 6-6 respectively
(M,T,W,T,F,S,S) = range(7)

## 3.5 formatting strings
k = 'uid'
v = 'sa'
## when using string substitutions each var %s then % (str1, str2)
'%s = %s' % (k,v)

## can also do this instead of str(int), it is type coersion
users = 6
print 'there are %d users' % (users,)

## for floats - f gives 6 decimals
'stock price is %f' % 50.45
## .2f gives 2 decimals
'stock price is %.2f' % 50.45

## can add a + in front after %, in front of .1-4
## .1f gets 1 decimal
'change since yesterday: %+.1f' % 1.44

## 3.6 mapping lists
# list comprehension - mapping a list into another list
## by applying a fxn to each element in the list
li = [1,9,8,4]
# [fxn(element) for element in list]
## doesnt change original, would need to assign
[elem*2 for elem in li]
li

# the list comprehensions in the 1st fxn we did
params = {'server': 'mpilgrim',
                    'database': 'master',
                    'uid': 'sa',
                    'pwd': 'secret'
                    }
['%s = %s' % (k,v) for k,v in params.items()]
## params.items takes a dictionary and turns into list of tuples
params.items()

params.keys()
params.values()

# this will return a list of all the ks in the dict turned tuple
[k for k,v in params.items()]


### 3.7 joining lists and splitting strings
# ex of joining a list from 1st fxn
## every item in this list seperated by a ;
## join only works on lists of strings - doesnt coerce
';'.join(['%s = %s' % (k,v) for k,v in params.items()])

# split a string into a list
# first join them
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ';'.join(li); s
s.split(';')
# now input the number of times you want to extract a string
# to get list of 2 strs put 1
s.split(';', 1)


### 4.1 apihelper.py
def info(object, spacing=10, collapse=1):
    '''
    Print methods and doc strings.
    Object input can be module, class,list, dict or str
    '''
    methodList = [method for method in dir(object) 
    if callable(getattr(object, method))]
    
    processFunc = collapse and (lambda s: ' '.join(s.split())) or (lambda s:s)
    
    print '\n'.join(['%s %s' %
    (method.ljust(spacing),
     processFunc(str(getattr(object, method).__doc__)))
    ])

