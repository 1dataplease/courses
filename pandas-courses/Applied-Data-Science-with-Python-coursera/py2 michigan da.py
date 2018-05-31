#to work on ipython notebook open shell
#ipython notebook
#1-5, shift+enter

#python - data acquistion, cleaning, dbs, hi-perform
#jupyter notebook, matplotlib

#pandas - similar to relational theory

#advanced querying and manipulation w/ pandas
# boolean masking, hierarchical dbing

#project - merge/clean, answer them, also numpy and scipy

# almost every company use ds to create products, serve customers
# skepticism, experimentation, simulation, replication
# needed for scientific inquiry 

# 1 explore/prep -  ex. mine health data
# 2 represent (tabular, text, graph) and tranform, 
# 3 compute w/ data - r, python, pipeline - may need to span several
# 4 data modeling - predictive/generalitive - predict sales, price, cost, election
# 5 data viz and presentation - charting, graphing, viz
# 6 meta activity - science about data science - understand what works/doesnt (training)

#1-6
#python background

#dynamically typed - var can be str on 1 line, int on another
# interactive, dont have to worry about syntactic def everytime
x = 1
y = 2
#print x+y
# if you use it in interactive mode instead of script, prints immediately
# online jupyter, sends code to machine in cloud, executes, sends back

# interpreter is stateful. variables exist b/w cells
# if u change in previous cell, can restart and run all

def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z
#print add_numbers(1,2,3)
#print add_numbers(1,2)

 #dont have to send return type, can also set None
#set default value for parameters, set last as none default
# all the optional ones need to come at end

#labelled parameters

def add_numbers(x,y,z=None, flag=False):
    if(flag):
        print 'Flag is true'
    if (z==None):
        return x+y
    else:
        return x+y+z
#print add_numbers(1,2, flag=True)
#print add_numbers(1,2,3)

#can assign variable to fxn,
# can pass that variable to others
a = add_numbers
#print a(1,2)


#1-7
#py types and sequences

#built in fxn type -
#str,none,int,float,fxn

#they have properties - can be data or fxns
#native kind of type

#tuple
x=(1, 'a', 2, 'b')
#is mutable
#can mix types in it

#list
#can change contents by append

#both are iterable
#slice - [start: stop, stepping]

#regular expression evaluation in text mining class

#str+list basics
name = 'chris'
name2 = 'bob'
n3 = name+' '+name2+' '+name2
#print n3.split()[2]

#dict
#need to give a key to get the value or map
dct = {'chris': 'mich', 'bob': 'osu'}
dct['ken'] = None
dct

#for name KEYS in y DICTIONARY
for key in dct:
    #print DICT[KEY]
    #prints the VALUES
    print dct[key],'\n'

#dict['val'] prints its key
dct['chris']

#dict.values prints all the keys
dct.values()

#prints each key:value as a tuple in a list
#dict->list
dct.items()

for value in dct.values():
    print value,'\n'

for key,value in dct.items():
    print key
    print value, '\n'

#unpacking tuple
x = ('t', 'do', 'tdo@gm')
#gives each value its own name
fname, lname, email = x

x = ('t', 'do', 'tdo@gm', 'us')
fname, lname, email, nation = x


#1-8
#strings

#in early internet was 256 latin chars, ascii
#add languages, math, emoji w/ unicode (> 1MM)

# purchase orders
sales_record = {'price': 3.24,
                'num_items': 4,
                'person': 'bob'}

#a string with {} as 4 wild-cards
sales_stmt = '{} bought {} item(s) at a price of {} for a total of {}'

sales_stmt.format(1,2,3,4)
sales_stmt.format(sales_record['person'],
                        sales_record['num_items'],
                        sales_record['price'],
                        sales_record['num_items'] * sales_record['price'])

#assignment from online


#1-9
#read from csv

import os
os.chdir('C:\\Users\\wainman\\Desktop\\tw\\classes\\1 python michigan data-analysis\\course1_downloads')
import csv

#if online
#%precision 2

#with open(file.csv) as csvfile
#    df = list(csv.DictReader(csvfile))

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

#prints row 0, row1, row2 (not the columns)
#it would be printed as [{'':1, 'col1': val},
#                        {'':2, 'col1':val}]
mpg[:3]

#this gets all the column names from row0
#each row is ['key1':'val1" ]
mpg[0].keys()

##FIND avg the city mpg across all cars in csv
##theyre all strings now, need to convert to float to do math

#float(row[col] for row in mpg)
#len(df) gives the # of rows
sum(float(d['cty']) for d in mpg) / len(mpg)

##FIND avg cityMPG grouped by # of cylinders

#1st, just get all the values from a column
#{4,5,6,8}
cylinders = set(d['cyl'] for d in mpg)

#set(dict['col'] for dict in list)

#iterate thru this set, 0,0
# then iterate thru all dictionary in list, add values

CtyMpgByCyl = []

#for each of 2,4,5,6,8
for c in cylinders:
    sumpg = 0
    cylinderTypeCount = 0
#loop through the rows
    for d in mpg:
#        if that row has cyl in the current 2,4,5,6,8 group
        if d['cyl'] == c:
#            add to the current sumpg
            sumpg += float(d['cty'])
#            add 1 to the count for that cyl group
            cylinderTypeCount += 1
#   at the end of that group, append (group, avg) to the list
    CtyMpgByCyl.append((c, sumpg / cylinderTypeCount))

##advanced - lambda and list comprehension
#SORT highest to lowest

#list.sort(key=lambda kv: kv[0])
CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

##FIND avg hiway mpg for diff vehicle classes

#create set of all the values in this column
# set(d[col] for d in df)
vehicleclass = set(d['class'] for d in mpg)

##iterate/look/go thru {2seater,compact,suv,etc}
HwyMpgByClass = []
for t in vehicleclass:
    sumpg = 0
    vclasscount = 0
#    set empty frame for end, set sum=0,count=0 at start of each class
#   for d in df:    
    for d in mpg:
#        if d['col'] == class
        if d['class'] == t:
#            add float(d[other col] to sum)
            sumpg += float(d['hwy'])
#            add classcount + 1
            vclasscount += 1
#    at end of class, append (class, sum/count)
    HwyMpgByClass.append((t, sumpg/vclasscount))

##SORT lowest to highest
#list.sort(key=lambda kv: kv[1])
HwyMpgByClass.sort(key=lambda x: x[1])


#1-10
#dates and times

#ex - helpful to find avg # sales over period, or period w/ most activity

# can be stored many ways - ipoc, 1/1/70 - s,ms since then
import datetime as dt
import time as tm

#get time in 12312312313.1 format
tm.time()

#a timestamp
#gets time in 500572 days since 1/1/70 format
dt.datetime(2016, 12, 15, 9, 24, 40, 500572)

#create the above timestamp but for today
dtnow = dt.datetime.fromtimestamp(tm.time()); dtnow

#get current day/time in english with below fxns
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second

#math - sub/add/compare. create a '100 days' variable
delta = dt.timedelta(days=100); delta

today = dt.date.today()

#gives today - 100 days
today-delta


#1-11
#advanced object orientation - map()

#classes w/ attached methods
#use them, less likely to create new classes (verbose)

#DEFINE a class
#first of each word capitalized usually - CamelCase
class Person:
    #class variable
    #variables shared across all instances/objects of Person - default  
    department = 'School of Information'
    
    #defining method
    #write as you would when making a function
    #need to include self as 1st parameter
    #pre-pen variables with word self
    
    #these change instance-bound variables name+location
    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

#havent created any objects yet
#call class name Person()
#then call fxns, print attributes of classes with dot notation

#full access to all methods/attributes
# can add constructor if you want - __init__()

#parameter for fxn can be fxn itself


#map(fxn to execute, something that can be iterated on)

#prices from 2 different stores on len(store1) items
store1 = [10, 11, 12.34, 2.34]
store2 = [9, 11.10, 12.34, 2.01]

#FIND minimum we would have to pay if we bought cheapest of each item
#run min on each index of all the lists given
#map will treat the 2 as if it was 1
cheapest = map(min, store1, store2)

#in py3 it prints a map object; common for bigdata, efficient memory

#use for loop to look at all values in the map object (in py3)
for item in cheapest:
    print item


#1-12
#advanced lambda and list comprehensions

#lambda is way of creating an anonomous fxn
#simple, short - write in 1 line

#declare fxn with "lambda", then list of args, then ":", then expression
# lambda arg1 arg2 arg3 : what it should do to args

#lambda ArgsItTakes: WhatItDoes
my_fxn = lambda a,b,c : a+b
my_fxn(1,2,3)

#cant have default values, cant have complex logic - 1 expression

#sequences are structures we can iterate over
#can create w for loop, etc

# abbreviated syntax - list comprehension

#common way
#empty list
my_list = []
#for n in 0-999
for number in range(0,1000):
    if number % 2 == 0:
        my_list.append(number)
my_list

#can rewrite this shorter as a list comprehension
#[i for i in range if i%2==0]

my_list = [number for number in range(0,1000) if number % 2 == 0]


#1-13
#numpy
import numpy as np

#make array
# can create list and convert it to array
mylist = [1,2,3]
x = np.array(mylist)

#quicker
x= np.array([1, 2, 3])

#make multi-dimensional array - list of lists
#each list is a ROW 
#comma demotes a NEW ROW
#each row needs to have SAME NUMBER OF COLUMNS/OBJECTS
m = np.array([[7, 8, 9], [10, 11, 12]])
m.shape

#can do a range - start, stop, step-size
n = np.arange(0, 30, 2); n

#convert above list into a 3x5 array, split into 3 lists of 5 items
#converts long list 0 to 28 to a 3X5 (can do, len(n=15)
#reshape(#rows, #columns)
n = n.reshape(3,5); n


#can put in start, stop, how many items you want in it
#linspace(start, stop, # of elements) -> 1d array
o = np.linspace(0, 4, 9); o

#change the last list into 3 rows 3 columns - similar reshape
o.resize(3, 3)

#create arrays of only 1s or 0s, fill in (ROW, COLUMN)
np.ones((3, 2))
np.zeros((2, 3))

#ones on only the diagonals of a square
np.eye(3)

#stretch a list of 3 into the diagonal values on a square
y = [1,2,3]
np.diag(y)

#array w/ repeated values
np.array(y*3)
#or use repeat, this prints 1 1 2 2 3 3 though
np.repeat([1,2,3], 2)

#combine arrays
p = np.ones([2, 3], int); p

#takes the above 2x3 of 1s and stacks it on top of one double that
print 'vstack:', np.vstack([p, 2*p]), '\n'

#same but stacked horizontally
print 'hstack:', np.hstack([p, 2*p]), '\n'

#operations
x= np.array([1, 2, 3])
y = np.array([4, 5, 6])

x+y
x*y
x**2

#linear algebra - dot product
x.dot(y)

#square the values of y - row1 original, row2 is squared
z = np.array([y, y**2]); z
z.shape
z.T

x.dtype
#turn an array from int to float
z = z.astype('f')

a = np.array([-6, -2, 1, 3, 5])

#sum this row
a.sum()
a.max()
a.min()
a.mean()
a.std()

#to find what index max is at
a.argmax()

#create an array with the squares of all values 0-12
s = np.arange(12)**2; s
s[4]
#prints an array 0 1 4
s[:3]

#5th from end -> beginning, count by 2
s[-5::2]

#2d array 0 - 35
r = np.arange(36)
r.resize(6, 6); r

#find value in row 2, col 2
r[2, 2]

#slice of row 3 and columns 3-6
r[2, 2:6]

#first 2 rows, all columns but last
r[:2, :-1]

#every 2nd element from last row
#needs comma in row, otherwise it selects whole row
r[-1, ::2]

#conditional indexing
r[r > 30]

#all the elements that were > 30 are now set to = 30
r[r>30] = 30; r

#new array, slice of r
r2 = r[:3, :3]; r2

#set all their elements to 0
r2[:] = 0

#looking at original r, can see its been changed too
r

#to create a copy that wont change original array
r_copy = r.copy()
r_copy[:] = 10; r_copy

# Iterating over arrays

#4x3 of random numbers from 0-9
#needs to have arguments(start, stop, (#r, #c))
test = np.random.randint(0, 10, (4,3))

#for row in test:
#    print row
#    
#for i in range(len(test)):
#    print test[i]

#can combine these 2 ways of iterating with enumerate
#gives us the row, index of row

#for Rowindex, RowContents in enumerate(array)
#do something to RowIndex, and to rowContents/rowList
for i, row in enumerate(test):
    print 'row', i, 'is', row

#new
test2 = test.copy() ** 2; test2

#to iterate thru 2 arrays, use zip
for i, j in zip(test, test2):
    print i, '+', j, '=', i+j

print '\n'



#2-1
#intro pandas
#wes mckinney - o reilly - python for data analysis
#matt harrison - learning the pandas library

#2-2
#series data structure

#series means that key is colName, values are values after it

#header
#special index like keys, and values

#create series by passing in values
import pandas as pd

#will have 0,1,2 as index in it still
animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)

numbers = [1, 2, 3]
pd.Series(numbers)

#if series is str, will keep None
animals = ['Tiger', 'Bear', None]
pd.Series(animals)

#for numbers/floats,  autoconverts none to NaN
#Not a Number
numbers = [1, 2, None]
pd.Series(numbers)

#NaN is not = none, not = NaN
import numpy as np
np.nan == None
np.nan == np.nan

#have to use np.isnan() to find out if something is np.nan
np.isnan(np.nan)

#below doesnt work, doesnt try to recognize a None converted to NaN
#np.isnan(numbers[2])

#series can be from dictionary data
#index is assigned to the keys you designed
#list of countries is the value of the series

#kept in dictionary
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'TKD': 'Korea'}

#create a series out of the above dictionary
s = pd.Series(sports)

#instead of 0-3 as index, it has it the 4 keys/indexes
s.index

#if you wanted to seperate index creation from data
#by passing in argument index = []
s2 = pd.Series(['Tiger', 'Bear', 'Moose'],
              index = ['India', 'America', 'Canada'])

#if u have more or fewer indices than values
# pandas will add nones to any keys or values missing


#2-3
#querying a series

#these are indexing operators to access series data
#by index position or index label
#theyre methods not attributes, so use sqr bracket not ()

#to find the 4th row's values use df.iloc[3]
s.iloc[3]

#int operator, performs same as if used iloc
#find 4th row
#only works if no catnames or labels are ints 
s[3]

#FIND by label or index name, use loc
#if your index is a list of integers
#pandas cant tell if youre querying by index position or label

#df.loc['index1']
s.loc['Golf']

#df['index1']
s['Golf']

s = pd.Series([100, 120, 101, 3])

#look at all values in series, do operation/fxn/transform
#can iterate, invoke operation

#for item in df: x+= item;
x=0
for item in s: x += item; x

#adds up all nums in series/column, just can be slow
total = 0
for item in s:
    total += item
print total

#vectorization - method of computation - parallel computing
# works w/ most fxns
#prints out as 324L annoyingly
total = np.sum(s); total

#create large series of random numbers
#np.random.randint(start, end, # of values created/inserted 
s = pd.Series(np.random.randint(0, 1000, 10000))
s.head()
len(s)

#magic functions - begin with % - if u run them together
#timing fxns

#if online
'%%timeit -n 100'
summary = 0
for item in s:
    summary += item
#100 loops, best of 3: 1.1 ms/loop

'%%timeit -n 100'
summary = np.sum(s)
## prints 100 loops, best of 3: 83 ms / loop

#broadcasting
#do an operation to every value in the series, changing them
#487 microseconds / loop

#the timer doesnt work in this example
#this will add 2 to all values in the series, very fast
s += 2
s.head()

#ALSO can do loop, slower
#for index,v in series.iteritems():
#    series.set_value(index, value+2)

#83 ms, slow
'%%timeit -n 100'
#for index,val in s.iteritems():
#    sets new value to be index, val+2
for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()

# .loc lets you modify and add new data to a series
# if the value you pass in doesnt exist, new entry is added
for label, value in s.iteritems():
    s.loc[label] = value + 2

#indices can have mixed types
#creates 0,1,2, animal as col; 1,2,3,bears as values
s = pd.Series([1, 2, 3])

#adds new row, index animals, value bears
s.loc['animal'] = 'bears'

#example where index values are not unique
#so dfs are different conceptually than a rdb might be

#new sports
sports = pd.Series({'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'TKD': 'Korea'})

#values in a list, then index values in a list
cricket_countries = pd.Series(['Australia',
                               'Barbados',
                               'Pakistan',
                               'England'],
                               index = ['Cricket',
                                        'Cricket',
                                        'Cricket',
                                        'Cricket'])

#append doesnt change original series
#returns new series made up on 2 appended together
#df1.append(df2)
#df1 stacked right on top of df2, no column name
all_countries = sports.append(cricket_countries); all_countries

#tutorial 


#2-4
#dataframe structure

## 2 dimensional series object or 2 axes labelled array
## each row has an index
## each col - .columns()

## you can access the index/row 2 with
#df.iloc(2)

## access just index 5 and column name
#df.loc(5)['Animals']
#
## get whole 2nd column 
#df['owners']

#3 purchase records for store
import pandas as pd

#this series is the row, it contains 3 columns(keys) each w 1val
purchase1 = pd.Series({'Name': 'Chris',
                       'Item Purchased': 'dog',
                       'Cost': 22.50})
                       
purchase2 = pd.Series({'Name': 'Kevin',
                       'Item Purchased': 'kitty litter',
                       'Cost': 2.50})

purchase3 = pd.Series({'Name': 'Vinod',
                       'Item Purchased': 'bird seed',
                       'Cost': 5.00})
                       
#instead of 1 dict, now feeding it 3 series in a list
# also adding a index for each of these 3 rows
df = pd.DataFrame([purchase1, purchase2, purchase3], \
index = ['store 1', 'store 2', 'store 3'])
df.head()

#select row using loc entering the index name
#the row is the above purchase2 series
df.loc['store 2']

#indices on rows or on columns can be repeated
#if 2 store1s, query for it gives a db of 2 rows

#find costs for store1
#df.loc['indexName', 'colname']
df.loc['store 1', 'Cost']
#df.loc['indexName']['colname']
df.loc['store 1']['Cost']

#'cost' column as a series
df['Cost']
#df['col'] = df.T.loc['col']
df.T.loc['Cost']

#T.loc is like locating a col instead of a index

#iloc and loc are used for ROW selection
#iloc is for entering row number (int)
#loc is for entering index name (string)

#if changing data, dont [][] (dont chain)
#returns a copy of dataframe instead of a view on it

#####sub-select 2 COLUMNS####
#df.loc[rows, ['col1', 'col2]]
df.loc[:, ['Name', 'Cost']]

#dropping data - input index/row_label
#use () not []

#this is a copy, df will still have the row
#need to put in inplace, or assign df to this
df.drop('store 1')

#first, copy df, assigning it to a df2
df_w_drop = df.copy()

#then df3 = df2.drop('col1')
df_w_drop = df_w_drop.drop('store 1')
df_w_drop

#set inplace=true, then u dont need to copy or assign dfs
#df.drop('rowIndex', inplace=True)
df_w_drop.drop('store 2', inplace=True)

#axis=0 IS ROW
#axis=1 IS COLUMN
#by default, the argument axes=0, dropping a row

# to drop a whole column, use axis=1
#df.drop('col', inplace=True, axis=1)
df_w_drop.drop('Name', inplace=True, axis=1)

#can also drop a column using del df['column']
#takes effect immediately, not a copy
#del df['col']
del df_w_drop['Cost']

#adding new column = [list of values]
#with 1 value as default
df_w_drop['location'] = None


##2-5
##dataframe indexing and loading

## 1. read csv into df -> reduce to cols/rows interested in

#can create series based on 1 column/category
costs = df['Cost']; costs

##in this series, increase all with broadcasting
costs += 2

#in original df, all those have risen (inplace)
##if using a copy to make changes, safer to do
df2 = df.copy()

import os
os.getcwd()
os.chdir('C:\\Users\\wainman\\Desktop\\tw\\classes\\1 python michigan data-analysis')

df = pd.read_csv('olympics.csv')

##can use shell command using ! in jupiter/linux/mac
##to look at a file: !cat file

#row1,col1 has an empty value in csv, returns as np.nan
df.head()

#№ is unicode
#need to read with the header
#also want to make the first column (country) an index
#also want to skip row1 which just has row number
df = pd.read_csv('olympics.csv', header=True, index_col=0,
                 skiprows=1)

#01 !, 02 !, 03 ! in front of winter/summer
#pandas appended .1, .2 to end of different olympics
#can change values of column names
df.columns

#for col in df.columns:
    #if colname string starts with these
#    if col[:] == 'start of col name':
        #df.rename(columns={OLD_NAME: NEW_NAME}, inplace=True)
#        df.rename(columns={col: 'this is name now'}, inplace=T)

#doesnt really work - csv isnt read same as in video
for col in df.columns:
    if col[:2] == '01':
#        set col parameter as a dict with key=OLDCol, value=NEW
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '#':
        df.rename(columns={col:'#' + col[4:]}, inplace=True)

df.head()
#
#
##2-6
##querying a dataframe
#
##boolean masking
##fast/efficient
## an array like 1d series of 2d dataframe, all True or False
## its overlayed with our array, any falses are not put in
#
##shows df and rows with countries that got old
#df['Gold'] > 0
#
##results are returned as booleans
##this builds us the boolean mask, 1/2 the battle
##now we want to overlay it on df using where fxn
#
##takes mask as condition, applys it to df, returns new one of same shape
#golds = df.where(df['Gold'] > 0); golds.head()
##only returns the values that meet the condition in the where
##all the rows that didnt meet the criteria have NaN across whole row
##Afghan has nan all across
#
##most stat fxns ignore values of nan
#
##now count countries with golds
#golds['Gold'].count()
#
##but on original df, it counts 147 instead of 100
##thats because it counts all the 0s
#df['Gold'].count()
#
##we often want to drop rows that have all nans / no data
#golds = golds.dropna()
#
##more concise example of getting just golds
##pandas alreadly filters out those rows with all nans
#df[df['Gold'] > 0]
#
##chain together complex queries to get single boolean mask
#
##create mask for all countries that got summer gold OR witer gold
#df[ (df['Gold'] > 0) | (df['Gold.1'] > 0)]
##can put len around that to see # of rows
#
##which country won winter gold but never summer gold
#df[ (df['Gold.1'] > 0) & (df['Gold'] == 0)]
#
##each mask needs to be in parentheses
#
#
##2-7
##indexing dataframes
#
##index is row-level label
##in olympics, it was name of country
##when we specify header or use dictionary
#
##set_index fxn - doesnt keep current index
#
##would need to manually create a new one, copy it in
#
##index by number of summer golds
#
##1st preserve the country info in a new column
##set country = existing index
#df['country'] = df.index
#
##set index to be the same as the gold column
#df = df.set_index('Gold')
#
##looks like 1st row was added w/ empty values
#df.head()
##but not the case
##empty is a None or NaN
#
##index has a name of gold
#
##can get rid of index completely, turns it into column
## and then creates a default numbering
#df = df.reset_index()
#df.head()

#can do multi-level indexing
# similar to composite keys
# call set_index(list of columns to promote to index)

#pandas will search thru them, find distinct data, form composites

#look at census.csv
df = pd.read_csv('census.csv')
df.head()
#population level data at us-county level

#summarized levels - country, state, county

#sim to sql distinct operator
df['SUMLEV'].unique()
#shows a list of only 2 values - ([40,50])

#get rid of all rows that are summaries at the state level
#just keep the county data
df = df[ df['SUMLEV'] == 50]
df.head()

#reduce columns to just total # of population estimates and total # of births
columns_to_keep = ['STNAME', 'CTYNAME', 'BIRTHS2015']
df = df[columns_to_keep]

#can set index to be combo of state and county

#create a list of columns we want to have indexed
#call set_index on it, assign output as df
df = df.set_index(['STNAME', 'CTYNAME'])

#QUERY this dataframe
#inside index, each col is called a level

#call all levels in mich
df.loc['Michigan']

#to call columns from wasada county
df.loc['Michigan', 'Washtenaw County']

#to compare 2 counties
#list of tuples describing indices we want to query
#df.loc[rowIndex] or df.loc['rowIndx1, rowIndx2] or df.loc[ [('',''), ('','') ] ]
df.loc[ [ ('Michigan', 'Washtenaw County'), ('Michigan', 'Wayne County') ] ]


#2-8
#missing values

#None and np.nan


#to turn off white space valuing - rare
#na_filter = True 

#when loading from csv: can do: na_values = 99
df = pd.read_csv('log.csv'); df

#video-watching stats, comes in every 30 seconds
#should be sorted by timestamp to see any sense
#missing values in columns - null if no changes

#can do either a NA value or fill method
#df.fillna(value = 'change all data to 1 value',
#         method = 'ffill') #or bfill if going backwards

#data needs to be sorted in order to use method
#ffill takes value from previous row
#bfill takes value from the next row

#sort by timestamp
df = df.set_index('time')
df = df.sort_index()
#but index is not unique, 2 users use sys at same time

#set back to how it was before when first imported it
df = df.reset_index()

# so instead, set index to 2 levels - time and user
df = df.set_index(['time', 'user'])

#dont need to sort again, it was already sorted by time

#fill in ALL NA values in w ffill
df.fillna(method = 'ffill')

#can fill in na w/ a column / series the same length as df

#stat fxns ignore missing values - mean will ignore them


#week2 assignment2


#1d series and 2d dataframe

#get row by index number
#df.iloc[0]
#get row by index name
#df.loc['firstID']

#['col'] for column
#df[df[col]>0] - boolean masking / filtering method

#pre 3-1 review
#reduce and process with
#groupby, apply, combine
#stats and ml


#3-1
#merging dataframes

#to add new data to existing df
#also have to add the index
#df['col'] = 1 value (scalar) or series

#to assign a diff value for every row
# list needs to be right len

df = pd.DataFrame([ {'Name': 'Chris',
                       'Item Purchased': 'dog',
                       'Cost': 22.50},
                       {'Name': 'Kevin',
                       'Item Purchased': 'kitty litter',
                       'Cost': 2.50},
                       {'Name': 'Vinod',
                       'Item Purchased': 'bird seed',
                       'Cost': 5.00}],
                       index = 
                       ['store 1', 'store 2', 'store 3'])

#add new col date with list of 3 values
df['date'] = [ 'Dec 1', 'Jan 1', 'mid-may']

#add new column or field that is a single, scalar value
df['delivered'] = True

#hard - only adding 2 values, also inputting a None
df['feedback'] = [ 'positive', None, 'negative']

#just example: reset index so dataframe is labeled 0,1,2
adf = df.reset_index()

#can create column without including Nones
#value 1 is automatically inserted as NaN
# so we can ignore the values we dont care about or have
#have to do as a dictionary
#pd.Series({index0: value,
#           index1: value})
adf['date'] = pd.Series({0: 'dec 1',
                        2: 'mid-may'} )
adf

#join 2 large dfs together
#create 2 dfs - play w/ combining/merging, venn diagram

pd.DataFrame([
{'col1': 'row1s value', 'col2': 'row1s value'},
{'col1': 'row2s value', 'col2': 'row2s value'}
])

#below, james and sally are both student+staff

#name and school columns
student_df = pd.DataFrame([
                        {'name': 'james',
                         'school': 'business'},
                         {'name': 'mike',
                         'school': 'law'},
                         {'name': 'sally',
                          'school': 'engineering'}
                          ])

#name and role columns
staff_df = pd.DataFrame([
                        {'name': 'kelly',
                         'role': 'director of hr'},
                         {'name': 'sally',
                         'role': 'course liason'},
                         {'name': 'james',
                          'role': 'grader'}
                          ])

#even if doubles, set name as index
student_df = student_df.set_index('name')
staff_df = staff_df.set_index('name')

#venn diagram - shows set membership
#students only / students+staff / staff only

#when you want to join them together, choices to make
#both dfs are indexed on name, the col we want to merge on

#list of all people, regardless of staff or student - all info
#union (set theory) = a full outer join

#use left (students) & right (staff) indices as the joining columns
#prints out name as index; role + school as columns
pd.merge(student_df, staff_df, how='outer',left_index=True, right_index=True)

# inner join; intersection in set theory
# list of ppl we have max info for, who are both student+staff
#only the rows we have student info and staff info
#prints out only james + sally, their name is listed in both
pd.merge(student_df, staff_df, how='inner', left_index=True, right_index=True)

#exs of set addition below

#want to get a list of all students
#regardless of if they were staff or not
pd.merge(student_df, staff_df, how='left',left_index=True, right_index=True)

#get a list of all staff
#regardless of if students or not
pd.merge(student_df, staff_df, how='right',left_index=True, right_index=True)

#dont need to join on indices, can join on columns
#this makes index back to numerical keys
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

#put left_on=COL; right_on=COL
#for left join, still prints only the list of staff
pd.merge(staff_df, student_df, how='left',left_on='name', right_on = 'name')


#what happens when we have conflicts b/w dfs

#create new staff and student, but have location cols
#kids home
student_df = pd.DataFrame([
                        {'name': 'james',
                         'school': 'business',
                         'location': '1024 billiard ave'},
                         {'name': 'mike',
                         'school': 'law',
                         'location': 'frat house 22'},
                         {'name': 'sally',
                          'school': 'engineering',
                          'location': '514 wilson crescent'}
                          ])
#office space
staff_df = pd.DataFrame([
                        {'name': 'kelly',
                         'role': 'director of hr',
                         'location': 'state st'},
                         {'name': 'sally',
                         'role': 'course liason',
                         'location': 'washington ave'},
                         {'name': 'james',
                          'role': 'grader',
                          'location': 'washington ave'}
                          ])
                          

#sally has home address in student, office in staff
#it will print address_x for student, address_y for staff
#location_x is for left df info
#location_y is for right_df info
pd.merge(student_df, staff_df, how='left', 
         left_on='name', right_on='name')

#df of products and invoices
#product and sticker price / ppl quantity
#have one listing all info, totals

#multi-indexing and multiple columns
#if first names overlap but last names dont
# use list of multiple columns to join on, not just on 1

#new one with last names added
student_ln = pd.DataFrame([
                        {'first_name': 'james',
                        'last_name': 'hammond',
                         'school': 'business',
                         'location': '1024 billiard ave'},
                         {'first_name': 'mike',
                         'last_name': 'smith',
                         'school': 'law',
                         'location': 'frat house 22'},
                         {'first_name': 'sally',
                         'last_name': 'brooks',
                          'school': 'engineering',
                          'location': '514 wilson crescent'}
                          ])

staff_ln = pd.DataFrame([
                        {'first_name': 'kelly',
                        'last_name': 'dejardins',
                         'role': 'director of hr',
                         'location': 'state st'},
                         {'first_name': 'sally',
                         'last_name': 'brooks',
                         'role': 'course liason',
                         'location': 'washington ave'},
                         {'first_name': 'james',
                         'last_name': 'wilde',
                          'role': 'grader',
                          'location': 'washington ave'}
                          ])

staff_ln
student_ln

#inner join on 2 columns - first AND last name
#who is both student+staff
#it doesnt include james wilde and james hammond
pd.merge(staff_ln, student_ln, how='inner', 
         left_on=['first_name', 'last_name'], 
        right_on = ['first_name', 'last_name'])


#3-2
#pandas idioms

#some ways more appropriate
#idiomatic solution - often hi performance, hi readability

#use vector instead of iteration / pandorable

#chain indexing
#generally bad, could return a copy or view ~ numpy
#if you see ][, think carefully
#df.loc['store 1']['Cost']
#df.loc[0]['Cost']

#method chaining
#every method on an obj returns a reference to that obj

df = pd.read_csv('census.csv')

#put many statements in 1
#cant do in py2
#(df.where(df['SUMLEV'] == 50)
#.dropna()
#.set_index(['STNAME', 'CTNAME'])
#.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

#can do in py2
## df.where[df['col']==condition]
df = df[df['SUMLEV'] == 50]
df.set_index(['STNAME', 'CTYNAME'], inplace=True)
df.rename(columns={'ESTIMATESBASE2010' : 'Estimates Base 2010'})

#map
#basis for functional programming
#takes fxn & iterable obj (like a list) to apply fxn to
#fxn is called on each item in list

#applymap
#provide fxn to operate on each cell of dataframe
# returns that df after fxn

# apply
#mapping across all rows in dataframe

# finds min and max of all rows in these cols, 
#returns new row
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.series({'min': np.min(data),
                      'max': np.max(data)})

## axis=1 is the parameter of the index
## to apply fxn to all rows 
#to find highest in column, axis=1

#below doesnt work in py2
#returns stname,ctyname, max,min
#df.apply(min_max, axis=1)

## can add that rows max and min as columns to df
## useful for building summary/desc stats in col
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row

df.apply(min_max, axis=1)

##rarely see apply with large fxns
##usually see apply with lambdas
#returns eachs rows max across these 5 columns
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis=1)


#3-3
# group by

#ASSIGNMENT 2 USED WITH INFO UP TO HERE

#iterate over all states, get avg population
#loop and unique ok, groupby is faster

#takes col names, splits df into chunks ~ names
# returns a groupby obj, can iterate
# then returns a tuple
#item1: group codition, item2: reduced df
# since it has 2 values, can unpack that tuple
#pick a column, get the average

import pandas as pd
import numpy as np
import os
os.getcwd()
os.chdir(r'C:\Users\wainman\Desktop\tw\classes\1 python michigan data-analysis')
df = pd.read_csv('census.csv')
df = df[df['SUMLEV'] == 50]

#iterate method
#df.where doesnt work in py2
'%%timeit -n 10'
#for state in df['STNAME'].unique():
#    avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
#    print 'Counties in state ' + state + ' have an avg pop of ' + str(avg)

#faster
'%%timeit -n 10'
#for group, grouped_df in df.groupby('col2split')
for group, frame in df.groupby('STNAME'):
#    avg = np.average(grouped_df['look at each groups this'])
    avg = np.average(frame['CENSUS2010POP'])
    print 'Counties in state ' + group + ' have an avg pop of ' + str(avg)

#can also do a fxn on groupby

#ex. work on 1/3 of states at time
#create some fxn that returns 0,1,2 ~ stname.str[0]
#tell groupby to use this fxn to split up df
#HAVE TO set index=col u want groupby first

#ex of fxn on groupby
#HAVE TO set index to the col we want to groupby
df = df.set_index('STNAME')

#this is a fxn on a string item, returns 0/1/2
def fun(item):
    if item[0] < 'M':
        return 0
    if item[0] < 'Q':
        return 1
    return 2

#pass fxn to df
#applys the above fxn to all of the indexes
# if 'stname' index starts with letter, return 0/1/2
#like a light-weight hashing
#used to distribute tasks across workers

#for group, each_df in df.groupby(grouping fxn):
for group, frame in df.groupby(fun):
#    print len(each_df)
    print 'There are ', str(len(frame)), 'records in group', str(group), 'for processing.'

#split-apply-combine
#split data, apply some fxn, combine the results

#groupby object has the aggregate method
#apply fxn to columns, return results
#pass in a dictionary of cols, and the fxn to apply
import numpy as np
df = pd.read_csv('census.csv')
df = df[df['SUMLEV'] == 50]

# Build a summary df w cols of avg popln for each state

#stname will be the index
#census2010pop the only column, has avg

#df.groupby('col2group').agg({'col2avg': fxn})
df.groupby('STNAME').agg({'CENSUS2010POP': np.average})

#potential issue
#when pass in a dictionary to
#1) id columns to apply a fxn on
#or 2) name an output column (if running multp fxns)

#difference depends on keys we pass in from dict

#also, theres a diff b/w a df groupby and a series groupby
#behave differently with agg

#this is a groupby dataframe
(type(df.groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011']))

#this is a groupby series
print(type(df.groupby(level=0)['POPESTIMATE2010']))

#Turn df to series w/ stname as index, cols is 2010pop
# groupit by index using level parameter
# call agg fxn using np.avg and sum
# since theres only 1 column of data, it applys
#both avg and sum to that column and prints it

#df.set_index('groupCol').groupby(level=0)['col2change']
#.agg({'newCol1': avg, 'newCol2': sum})
#level=0 groups it by the index instead of putting in colName
df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg(
    {'avg': np.average, 'sum': np.sum})

#in PY3, can do same on a whole df instead of on a column/series
# set index= stname, groupby index, project 2 columns
# call agg w 2 parameters, avg and sum

#doesnt work in py2
#df.set_index('STNAME').groupby(level=0)[(['POPESTIMATE2010', 'POPESTIMATE2011'])].agg(
#{'avg': np.average, 'sum': np.sum})


#3-4
#scales

#can support computational datatypes, is grade1/2 same as 7/8
#is diff a- b+ same as c- c?

#4 scales worth knowin

#ratio scale
#units equally spaced
#math operations of +/-/* all valid
#height and weight

#interval scale
#units equally spaced
#no such thing as a true 0, never missing
# can only do + and -
#temperature - always there, and 0 doesnt mean its gone
#direction on compass - 0deg is up, not missing

#ordinal scale
#order of units are important
#units or differences b/w values are not evenly spaced
#distribution of letter grades could be 3/4/3

#nominal scale
#categories of data
#limited number
#changing order - meaniningless
#teams of a sport
#if only 2 values - binary

#nominal/categorical data
#set it with astype

df = pd.DataFrame(['A', 'B', 'C', 'D'],
                  index=['excellent', 'ok', 'passing', 'poor'])

#df.rename(columns={colnumber: 'colname'})
df.rename(columns={0: 'grades'}, inplace=True)

#df[col].astype('category'
#categorys=[order low to high], ordered=T)
grades = df['grades'].astype('category',
    categories = ['D', 'C', 'B', 'A'],
    ordered=True)
    
#now we filter / create bool mask if grades better than C
grades > 'C'

#now we can look at all the grades that were better than C
grades[grades>'C']
np.min(grades)

#getdummys converts from single to 0/1

#REDUCE value from integer ratio to a categorical col

#histograms used with converted numerical data
#ML classification approach/categorization

df = pd.read_csv('census.csv')

#take only counties
df = df[df['SUMLEV'] == 50]

#set index to statename, groupby index
#take pop column and get the avg of all the rows in that state
df = df.set_index('STNAME').groupby(level=0)\
['CENSUS2010POP'].agg({'avg': np.average})

#cut takes column/df, and the # of bins to split it in
#it splits it into 10 equally sized/spaced categories
pd.cut(df['avg'], 10)

#if you want to split based on frequency so
# num of items in each bin is the same (instead of the spacing)

#graphing/charting: technique ~ data shape & goal of data

#3-5
#pivot tables, stats

#makes heavy use of the agg fxn
#pivtable - cells are some agg value
#can have marginal values - sums for each col,row

df = pd.read_csv('cars.csv')

#compare the battery by year and make
#row is year, col is make, values are the battery
df.pivot_table(values='(kW)', index='YEAR', columns='Make',
               aggfunc=np.mean)

#can pass in more than just avg at once
#can also ask for minimum, etc to display in same table
#margins adds All column - mean for year, min for year
#and mean for vendor, min for vendor

df.pivot_table(values='(kW)', index='YEAR',columns='Make',
               aggfunc=[np.mean, np.min], margins=True)

#3-6
#time series and date fxn

#4 time classes
#timestamp, datetime_index, period, period_index

#timestamp is single timestamp
#associates values w points in time
#interchangable with pythons datetime
pd.Timestamp('9/1/2016 10:05AM')

#period is across a day or month
pd.Period('1/2016')
pd.Period('3/5/2016')

#index of a timestamp

#create example series of time values
#pd.Series([val1,val2], [val1,val2])
t1 = pd.Series(list('abc'), 
               [pd.Timestamp('2016-09-01'), 
                pd.Timestamp('2016-09-02'),
                pd.Timestamp('2016-09-03')])
t1

#each timestamp is index, has a value

#the type of this series' index is datetime_index
type(t1.index)

#create a periodIndex
t2 = pd.Series(list('def'),
               [pd.Period('2016-09'), 
                pd.Period('2016-10'),
                pd.Period('2016-11')])
t2
#tseries.period.PeriodIndex
type(t2.index)

#HOW to convert to datetime
d1 = ['2 june 2013', 'aug 29 2014', '2015-06=26',\
      '7/12/16']

#dataframe with dates, values, dates are messy
#random.randint(start, end, (4#rows,2#cols))
#index=4dates, columns = ['a'col1, 'b'col2]
ts3 = pd.DataFrame(np.random.randint(10,100, (4,2)),
                   index=d1, columns=list('ab'))
#fix dates
ts3.index = pd.to_datetime(ts3.index)

#if you want day to be first, like europe
pd.to_datetime('4.7.12', dayfirst=True)

#timedeltas are differences in time
pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016')

#find date 12days,3hrs later
#doesnt work in py2
#pd.Timestamp('9/3/2016 8:10AM') + pd.Timedelta('12D 3H')

#9 measurements taken biweekly sunday oct 2016
dates = pd.date_range('10-01-2016', periods=9,
                      freq='2W-SUN')
dates

#create df w these dates, some random data
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5,10,9).cumsum(),
                   'Count 2': 120 + np.random.randint(-5,10,9)},
                    index=dates)
df

#check what day of the week a specific date is
#not in py2
#df.index.weekday_name

#diff - find difference b/w each days value
df.diff()

# FIND the mean count of each month in df
#in py2, that only gives the mean of each row
df.resample('M').mean()

#partial string indexing to find values from particular year
df['2017']

#values from a month
df['2016-12']

#slice on range of dates. dec/16 onward
df['2016-12':]

#change freq of our dates in our df
#change biweekly to weekly, have new ones filled in from prev
df.asfreq('W', method='ffill')

#plotting time series
import matplotlib.pyplot as plt

#only do the below when plotting in ipython or notebook
#%matplotlib inline
df.plot()


## WEEK 4 ##

# 4-1, 4-2
#intro course project
#distributions

#distribution: set of all possible random variables

#1 - a binomial distribution (2 outcomes possible)
# ex. flipping coins for heads or tails
# discrete (categories of heads and tails, no real numbrs)
# evenly weighted (heads as likely as tails)
# collect # of heads, # of tails, roughly equal
#  result of each flip is a random variable

#ex2. tornado events in city
#discrete - yes or no
# evenly weighted (tornados are rare)

#ask for a number
#np.random.binomial(# of simulations, likelihood of a 0)
np.random.binomial(1, 0.5)
