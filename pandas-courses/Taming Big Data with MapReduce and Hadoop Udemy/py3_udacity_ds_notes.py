# -*- coding: utf-8 -*-
"""
Created on Mon May  1 09:31:24 2017

@author: wainman
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#15-numpy
numbers = [1,2,3,4,5]
np.mean(numbers)
np.median(numbers)
np.std(numbers)

#16 - store and reference using pandas
#make df from scratch

#df is {'colname': pd.series([row1val, row2val, etc]),
#        'colname2': pd.series([row1val, row2val, etc])}
d = {'name': pd.Series(['Braund', 'Cummings', 'Heikkinen', 'Allen'],
     index=['a','b','c','d']),
     'age': pd.Series([22,38,26,35], index = ['a','b','c','d']),
    'fare': pd.Series([7.25, 71.83, 8.05], index=['a','b','d']),
    'survived': pd.Series([False,True,True,False], index=['a','b','c','d'])}

df = pd.DataFrame(d); df


#17,18, creating avg gold medal
countries = ['Russia', 'Norway', 'Canada', 'US']
gold = [13,11,10,9]
silver = [11,5,10,7]
bronze = [9,10,5,12]

olympic_medal_counts = {'country_name': pd.Series(countries),
                        'gold': pd.Series(gold),
                        'silver': pd.Series(silver),
                        'bronze': pd.Series(bronze)}

olympic_medal_counts_df = pd.DataFrame(olympic_medal_counts)
#find avg
np.mean(olympic_medal_counts_df.gold)


#19 - df columns
df['name']

#grab name and age, get multiple columns
df[['name', 'age']]

#call specific rows w index; get row by name; get row by number
df.loc['a']
df.iloc[0]

#rows where age>=30
df[df.age >= 30]

#pick out column1 that matches criteria2
df[df.age >= 30]['survived']
df['survived'][df.age >= 30]


#20
#operate on df in vectorized item-by-item way
#means apply a fxn like mean

d = {'one': pd.Series([1,2,3], index=['a', 'b', 'c']),
    'two': pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])}

df2 = pd.DataFrame(d)

#apply works on every column, creates a df; get mean of every col
df2.apply(np.mean)

#map on columns
#asks whether in this column, if its > 1, return T/F
# col.map(lambda each: each >=1)
#this returns a boolean mask
df['fare'].map(lambda x: x>=1)
df2['one'].map(lambda x: x>= 1)

#to do it over every value in df, same but applymap
#applymap on entire df
# would work if df only strs/ints
df = df[['age', 'fare']]
df.applymap(lambda x: x>= 1)

#21,22
#count the number of bronzes earned by countries w >= 1 gold
bronze_at_least_one_gold = olympic_medal_counts_df\
['bronze'][olympic_medal_counts_df.gold > 0]

avg_bronze_at_least_one_gold = np.mean(bronze_at_least_one_gold)
avg_bronze_at_least_one_gold

#mean of every int/float column
#creates new df showing age: mean(age)
df[['age', 'fare']].apply(np.mean)


#23,24
#new df showing avg num of gold, silver and bronze of gold>=1
golders = olympic_medal_counts_df[olympic_medal_counts_df.gold > 0]
avg_medal_count_if_gold = golders[['gold', 'silver', 'bronze']].apply(np.mean)

#25 - matrix multiplication and np.dot
# get dot product bw 2 vectors
a = np.array([1,2,3,4,5])
b = np.array([2,3,4,5,6])
#mult these matrices gives 1*2 + 2*3 + 3*4 + 4*5 + 5*6 = 70
a.dot(b)

# [1, 2] [2 4 6
#          3 5 7]
e1 = np.array([1,2])
e2 = np.array([[2,4,6], [3,5,7]])
# [1*2  + 2*3 
# 1*4  + 2*5
# 1*6  + 2*7]
# one array length 3
# 8, 14, 20
e1.dot(e2)

## again
e3 = np.array([[2,4,6], [3,5,7]])
e4 = np.array([8,9,10])
#            [8
# [2 4 6     9
# 3 5 7] *   10]

# [2*8 + 4*9 + 6*10
# 3*8 + 5*9 + 7*10 ]
e3.dot(e4)



# 26 - olympics medal points
# reused minor lists created in 17/18
countries = ['Russia', 'Norway', 'Canada', 'US']
gold = [13,11,10,9]
silver = [11,5,10,7]
bronze = [9,10,5,12]

olympic_medal_counts = {'country_name': pd.Series(countries),
                        'gold': pd.Series(gold),
                        'silver': pd.Series(silver),
                        'bronze': pd.Series(bronze)}
olympic_medal_counts_df = pd.DataFrame(olympic_medal_counts)

# get their scores given 4pts,2pts,1pts
olympic_medal_counts_df['score'] = olympic_medal_counts_df.bronze + \
       olympic_medal_counts_df.silver*2 + \
       olympic_medal_counts_df.gold*4
olympic_medal_counts_df



#27 - using dot fxn instead
medals_df = olympic_medal_counts_df[[0,2,3]]
# dot prod of a df and a series makes a series
points = medals_df.dot([1,4,2])


#dict
olympic_pts = {'country_name': pd.Series(countries),
               'points': pd.Series(points)}
olympic_pts_df = pd.DataFrame(olympic_pts)
olympic_pts_df



#28 - pandas - manipulate data for analysis. puts r in python

#29 - df is 2d. cols can be str or int or bool etc
df = pd.read_table('data/titanicPassengers.txt', sep = ',')
df

# can get row with 
df.loc[0]



#30 - create new df
d = {'one': pd.Series([1,2,3], index=['a', 'b', 'c']),
     'two': pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
df

# apply
# run fxn on every column
df.apply(np.mean)

# map
# run it on a series
# find all the ROWS with value > 1
# this question returns a boolean mask
df['one'].map(lambda x: x>=1)

#applymap
# runs on a df, runs on every col
# would require all cols being same dtype as question requires
df.applymap(lambda x: x>=1)

# 1-31 - lesson project - the titanic
# class / sex / age
# build a few models - predict survivors

#1-32 - class project - subway ridership
# require internet, use wunderground api
# weather -> num riders>
# time -> num riders?
# graphs, try to predict with regression

#1-33 - advice
# passion for a specific data
# or for patterns in data, try to find answers

#1-34 - advice 2
# curious, ask ?s, formulate as pertinent to themselves
# problem in general, make guesses as to causes, how to predict



#2-1 - lower-level - extract / clean / munge / wrangle data
# up to 90% of time spent on it
# ex. why ppl live longer in 1 city
# pull from site, store to a db, look at missing/weird -> clean / munge it

# lastfm
# acquire, inspect


#2-3 - what is wrangling
# figure out if l/r meaningful batting avg difference
# cant have > 1, cant have missing l/r

# get from files, db, websites/apis

#2-4,5 - analyzed messy data
# exs: reading reciepts, budget in spreadsheet
# tools - excel, pandas, folders, 

#2-7 - acquiring
# txt files like from govt
# seanlahman

#2-8 data formats
# csv - col is diff info on them, playerID, managerID , ,
# xml
#<document element>
#    <table>
#    <lahmanID> 1 </lahmanID>
#    <playerID> aaron </playerID>
## json
# can have nested structures
#{
#        'lahmanID' : 1,
#        'playerID': 'arron01',
#        'managerID': ''}
# wunderground is a json object
# xml similar to json
# datawrangling w mongodb - udacity


##2-9 - csv1
# importing to pd
# df['col]
# df[f] + df[f2]

## 2-10 - csv2 - write to new csv file
# sep, na=

## 2-11 - load csv into python
## takes csv, new_csv
## read-in, create nameFull, export it

## 2-13 - rdbs

## 2-14 - aadhaar
## like a ssn

## 2-15 - db useful
# easy to extract aggregated data w complex filters
# db scales well
# ensures data is consistently formatted
# no redudant data
# proven, used all over

## 2-17
# 1 table - agency, state, district
# related table could have info on districts - popln, size

## 2-18 - schema
# for a table, every row will have same num cols, samae values, formatted
# str, str, float, int
## set to NULL or default values

## 2-20 - 
# if put in a number, it would store it as a str in that column
# but cant do math on it

## 2-21 - simple queries
#select * from aadhaar_data
# limit 20;

## 2-22 -
#read in csv to df
# from 1-30
df2 = df.copy()
df2['one col'] = df2.one
df2['TWO col'] = df2.two
df2
   
#rename cols replacing ' ' w '_'
#set all chars to lowercase
df2.rename(columns = lambda x: x.replace(' ', '_').lower())

##select first 50 rows for registrar and enrollment_agency
answer222 = 'select registrar, enrollment_agency from aadhar limit 50;'


## 2-24 - complex queries
ex24 = "select * from aadhar where state='Gujarat'"
# aadhaar_generated is 1,1,1 etc.
ex25 = "SELECT district, subdistrict, sum(aadhaar_generated) \
FROM aadhaar \
WHERE age >= 60\
GROUP BY district, subdistrict"

## 2-26 - write one
# how many men and how many women over 50 have one in EACH DISTRICT
ans26 = '''SELECT gender, district, count(id)
FROM aadhaar
WHERE age > 50
GROUP BY gender, district'''
#execute26 = execute_sql(ans26)


#2-27 - apis, app programming interface, access twitter data
## webvrawler - complicated, blocked
# representational state transfer or REST

#2-29 - lastfm web services rest requests
lastfm_api_root_url = 'ws.audioscrobbler.com/2.0'

# how to get to data from lastfms api
# copypaste below into chrome, itll show junky data
paste_this_lastfm_link_in = "http://ws.audioscrobbler.com/2.0/?method=\
album.getinfo&api_key=[API_KEY]&artist=Rihanna&album=Loud&format=json"


##2-30 - json
#think of it as a dictionary
# each col is a key
# each val a val

##2-31 - dont have to type into browser everytime
import json
import requests

url = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&\
api_key=4beab33cc6d65b05800d51f5e83bde1b&artist=Cher&album=Believe&format=json"
try:
    raw_json_data = requests.get(url).text
    type(raw_json_data)
    # returns exactly the same json data that was in the browser
    raw_json_data
    # hard to parse out info like \/ - use json library
    data_dict = json.loads(raw_json_data)
    type(data_dict)
    data_dict
    # get the value for one of the cols/attributes/keys in the dict
    data_dict['artist']
except:
    pass


##2-32-33 - find top artist in spain
## pass in country parameter
## register for own API key here
api_key_site = "http://www.last.fm/api/account/create"
import json
import requests

# changed parameters, want geo.gettopartists
# country
url = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&\
api_key=4beab33cc6d65b05800d51f5e83bde1b&format=json"
try:
    # make our api call using requests library
    raw_json_data = requests.get(url).text
    type(raw_json_data)
    # returns exactly the same json data that was in the browser
    raw_json_data
    # hard to parse out info like \/ - use json library to load into a dict
    data_dict = json.loads(raw_json_data)
    type(data_dict)
    data_dict
    # get the value for one of the cols/attributes/keys in the dict
    data_dict['topartists']['artist'][0]['name']
except:
    pass



## 2-34 - sanity checking the data
# does data make sense? problem? does it look as expected?
# plots, analyses - exploratory da
# describe

## 2-35 - describe fxn
baseball = pd.read_csv('data/Master.csv')
baseball.describe()
# returns a df
# for every number col, we see count row, mean row, std, min, max, 25, 50, 75
# can see count is diff for every col, what to do about missings?


#2-36 - missing cuz
## might just not have it, noone wrote it down or knew or asked
# system errors
# some subjects/event types are systematically missing dtypes
# someone missed streets

#2-38 - collection technique causing missing data
# if failed 1/1000 times, or service outages
# if for example, all pitchers didnt have BA in, invalidates findings

#2-39 - if missing at random

#1. partial deletion - limit to data we have
# if wanted to know avg years and height - cant include alive ppl

#1a. listwise deletion
#  anyone missing deathdate OR height left out

#1b. pairwise deletion 
#  treat each var different - calculate all dead avg lives, and all avg heights



#2-40 - imputation - why impute
# dont throw out tons of rows
# impute if not much data
# or if removing rows affects representativeness

# make intelligent guess/approximation of missing values
# many techniques - each introduces certain biases. want robustness


#2-41 - easy imputation
# plug in the mean weight for everyone
# whats good - dont change the mean
# but if X weight -> height, it lessens the correlation

#2-42 - linear regression to estimate missing values
# create equation to fill in missing values
# more accurate
# drawback - overemphasize existing trends in data
# all imputed values amplifies trend
# suggests greater certainty than we have
# could train linear model on existing data, plug into missings

#2-43-44 - impute exercise
# df[col] = df[col].fillna(replacements)
baseball.weight.sum()
baseball.weight.mean()
baseball.weight = baseball.weight.fillna(baseball.weight.mean())
baseball.weight

#2-45 - other methods exist
# simple, effective, can amplify or nullify pre-existing trends in data


#2-46 - assignment2
#api - ny underground data
# use sql to run queries
# mta subway - clean and process



##3-1 methods for ml
# before: tallest ss, how many ppl >65
# now: all L > R
# corr age and rejection rate?
# time/weather -> num ppl subway

#3-2 - statistical rigor 1
# significance test
# using our data, can we disprove an assumtion w a pre-defined level of confidence?

#ex. all 10 say blue of 1000 ppl


#3-3 - no sig difference, see there is one
# a/b test for weeks, 5k in each. 50% and 50.5%
# 95% cl, ss but small difference

#3-5 - why stats useful in data science
# make sure reasonable inferences from data
# understand CIntervals, dont overinterpret

#3-6 - statistical significance tests useful cuz
# formalized framework for comparing and evaluating data
# evaluate whether perceived effects in our dset reflect differences across pop

# diff tests have diff assumptions about our data


#3-8 - compare BA of l vs R
# statistical signifance tests
# many make an assumption about the distribution of your data

#CLT
# very common: normal / gaussian / bell / z curve
# if an event is the sum of other random events, it'll be normal
# exs
# measurement errors, light intensity, blood pressure

#3-10 - normal dist
# 2 parameters - (location) mean/mu and (scale) sd/sigma

# probability density fxn description
# can be defined for any continuous data
# use it to determine probability that ppl are between 2 heights
# even though theoretically infinite values with many decimal pts
import math
import scipy.stats
# my attempt
def my_prob_of_pt_occuring(x_value, mean, sd):
    prob_x = 1/(math.pi * math.sqrt(mean))\
               *math.e^(-(x_value - sd)^2/(mean))
    return prob_x

def prob_of_pt_occuring(x_value, mean, sd):
    var = sd**2
    denom = (2*math.pi*var)** .5
    num = math.exp(-(x_value-mean)**2 // (2*var))
    prob_x = num/denom
    return prob_x

prob_of_pt_occuring(288, 300, 5)
scipy.stats.norm(300,5).pdf(288)
prob_of_pt_occuring(300, 300, 5)
scipy.stats.norm(300,5).pdf(300)


#3-13 - # T-TEST
# most common parametric test to compare 2 sets of data - if therse a ss diff
# such as samples of left/right (both normal dist) - is there a ss diff 

# is a statistical test
# accept or reject a null (assume no diff bw anything) hypothesis
# a null hypothesis is a stmt we want to disprove

#ex2 of an application of t-test
# that a sample is drawn from NORMAL dist
# can repeat, test it on each type of distribution

# if we had 20 heights and weights of players
# test how likely it is those 20 are drawn from our known complete player popln

# usually do a t-test or stat significance test on a test stat like mean
# it outputs a number t
# that number t can tell us if null hypo is true

# one-sample t-test
# our population mean MU = our sample mean MU0 or MUnought

# two sample t-test
# our 2 population means are equal; MU0 = MU1



#3-14 - welch's 2 sample t-test
# class project will have 2 samples (ie 2 populations / things)

# a few different versions of the t-test, depending on assumptions

# ex assumptions
# are the 2 population samples the same size?
# do the 2 population samples have the same variance?


#1 - welchs t-test
# compute a t-statistic with this eqn
def get_welchs_t_stat(mean1, var1, n1,  mean2, var2, n2):
    t_num = mean2 - mean1
    t_denom = math.sqrt(var2/n2 + var1/n1)
    t = t_num/t_denom
    
    nu_num = (var2/n2 + var1/n1)**2
    first_part_denom = (var2**2) / ((n2**2)*(n2-1))
    second_part_denom =  (var1**2) / ((n1**2)*(n1-1))
    nu = nu_num / (first_part_denom + second_part_denom)
    "then somehow these 2 are combined to get a p-value"
    '''p-value is the prob of obtaining a test-stat t
    at least as extreme as ours if null hypot was true'''
    return (t, nu)

'''nu = size-1
is the degrees of freedom associated with ith variance estimate'''

# set a critical value of p, p-critical
# if p < p-critical, then reject the null hypothes
# else, cannot reject the null hypothesis



#3-15 - calculating t and v
# what are the values of t and v given this data
get_welchs_t_stat(.299, .05, 150, .307, .08, 165)
# t-stat: how extreme is our result; how likely to disprove null hypoth
# nu: how many INDEPENDENT variables went into calculating this t-value



#3-16 - welchs t-test in python
# simpler than above
'scipy.stats.ttest_ind(list1, list2, equal_var=False)'
# welches t-test is when 2 lists have different POPULATION variance 
#if set it to true, then its a 1 sample t-test

# also, this assumes that performing a 2-sided t-test
# only testing that the 2 samples means are different

# how to perform a 1-sided t-test instead?
# IE test if 1 mean is greater than the other one?
# can just divide outcome of ttest by 2?????

#3-18 - one-sided welchs t-test in python
# with normal distributions (welches), 1-sided p-val is 1/2 of 2-sided p

# p-val is prob that given null hypothesis is true, we'd observe this or extremer

# if checking if mean2 > mean1, want t-val > 0
# if checking if mean2 < mean1, want t-val < 0



#3-19 - welchs ttest exercise
def compare_averages():
    '''
    performs a t-test on two sets of baseball data (lefties and righties)
    1st - run welchs t-tst on 2 throwing groups/cohorts
    2nd - if no diff, return (True, (t-val, nu/df?))
    2nd B - if diff, return (False, (t-val, nu/df?))
    '''
    # get a df that has both the throws and the batting data
    batting = pd.read_csv('data/Batting.csv')
    baseball = pd.read_csv('data/Master.csv')
    
    # only thing we need from batting (each row a season) is h/ab PER HITTER
    # NOT per season
    hitters = batting.groupby('playerID')[['H', 'AB']].sum()
    hitters['avg'] = hitters['H'] / hitters['AB']
    
    # now add baseball (containing L/R) to right of hitters df (containing avg)
    b2 = hitters.merge(baseball, how="left", left_index=True, right_on='playerID')
    # this makes index 0-num instead of name (like hitters was), is ok
        
    # these are the Xs
    lefties = b2[b2.throws == 'L']
    righties = b2[b2.throws == 'R']
    
    #these are the Ys
    lefties_avg = lefties.avg
    righties_avg = righties.avg
    
    #1 - run t-test
    # to work, the 2 series' Ys need to be nums?
    # so we compare the 
    
    ## assume diff variance of avgs (not positive if true)
    ## doesnt work with this data - 
    ## RuntimeWarning: invalid value encountered in greater
    ## return (self.a < x) & (x < self.b)
    #result = scipy.stats.ttest_ind(lefties_avg, righties_avg, equal_var=False)
    
    ## 
#    if result[1] <= .05:
#        return (False, result)
#    else:
#        return (True, result)
#compare_averages()
batting = pd.read_csv('data/Batting.csv')
baseball = pd.read_csv('data/Master.csv')

# only thing we need from batting (each row a season) is h/ab PER HITTER
# NOT per season
hitters = batting.groupby('playerID')[['H', 'AB', 'HR']].sum()
hitters['avg'] = hitters['H'] / hitters['AB']

# now add baseball (containing L/R) to right of hitters df (containing avg)
b2 = hitters.merge(baseball, how="left", left_index=True, right_on='playerID')
# this makes index 0-num instead of name (like hitters was), is ok
    
# these are the Xs
lefties = b2[b2.throws == 'L']
righties = b2[b2.throws == 'R']

#these are the Ys
lefties_avg = lefties.avg.dropna()
righties_avg = righties.avg.dropna()


#3-21 - what about prob distributions / non-normal data?
## this tools application to this specific data is also broken

# 1 - determine if data is normal - plot histogram

# is lefties avg normal?
# way 1 - hist, but would need to changes axes, bins, etc
import matplotlib as plot
lefties_avg.hist()
righties_avg.hist()


# 2 - statistical test to measure liklihood that sample is from normally dist popln
#    shapiro-wilk test
w, p = scipy.stats.shapiro(lefties.avg)
w, p
# w is nan, p is 1! so def normal?
# w is the shapiro wilk test-stat
# p-value 1 means 100% chance null hypo that dist is normal is true?
# liklihood of observing a value of w at least as extreme as NAN?



#3-22 - non-parametric tests
# some math says if samplesize large enough, can use tests that assume normal
# would prefer non-parametric test tho

# a statistical test that does not assume our data is drawn from any
# particular underlying distribution

#ex1 - mann-whitney U test / mann-whitney wilcoxan test
# tests the null hypothesis that 2 populations are the same

# p is the prob null hypothes that grp1 and grp2 are from same 'popln'
# doesnt test that 1 has a higher mean/median
# so useful to also include the 2 sample means

u, p = scipy.stats.mannwhitneyu(lefties_avg, righties_avg)
u, p
# this time got an actual answer
# u value is super large
# p value is 1-sided (not 2-sided)incredibly small
# suggests that lefties and righties avgs are from same population



# 3 - non-parametric test is a statistical test that
# does not assume data is drawn from any 
# particular underlying probability distribution



# 3-26 - predicting future data
# ML - ai focused on constructing systems that learn from large data to predict
# regressions / classification

#3-28 - ml useful because
# diff b/w stats and ml?
# ml came from cs. ppl had practical/product questions, tools for them
# most effective ways to make decisions ~ data
# ml - making accurate predictions
# dont care about assumptions as much as long as it works

# converging now
# stats focused on analyzing existing data, drawing valid conclusions
# are L > R - probability models


#30 - types of learning
# feed data into model, make predictions from it

# supervised learning
#use TRAINING data of 100 emails spam/not spam
# use TRAINING data of 100 houses' sq ft, prices, etc

# unsupervised learning - no training labels
# try to understand structure of data
# split photos into groups - ppl, horses, etc
# may not know what they are, just that theyre distinct

# fav ml algo
# loosely defined, broad understanding / hi level
# ex how ppl use social networks
# clustering - kmeans, heiarchical 

# other dimensionality reduction techniques
# Principal Component Analysis - get most meaningful factors/vectors
# plot those clusters on

#3-32 - predicting w regression
# write eqn that takes (height/weight/year/pos), predicts HR
# takes in these datapts
# build eqn w input variables
# use eqn to predict for players that werent in the training data

# gradient descent is an ex of linear regression

#3-33
# n many factors/cols we choose
# m rows / datapoints / target labels / Ys
# n*m total datapoints used in TRAINING data

# multiply each col/variable/factor by some set of coefficients
# can call those coefficients thetas or parameters or weights of model
# tell us how important each factor/input variable is
# theta1 * x1 + theta2 * x2 _ ... = Y

# green line is a straight line
# minimize the eqn across all datapoints

# find thetas to minimize these errors

# value to describe total errors of our model
# sum all ypredict - yreal
# square it so that very wrong one is worse than 2 medium bad predictions
# 2 and 0 off means 4;
# 1 and 1 off meaning 1, much better model



# 3-34-35
#Xs: age,weight, height Y: ba

#3-36 - use algo called gradient descent
# 1st define cost fxn: J(big theta) entire set of thetas

# same as
# = sum(ypred - yreal)**2

# J(bigTheta) = 1/2 * sum(ypred - yreal)**2

# ypred_of_xi = sum(thetaN * xni)
# sum up each input var xn * each weight theta

# include n=0
# same as thetaTranspose * x



#3-37 - lin reg w gradient descent
#how to minimize J(bigTheta)
# keep trying new values of THETA until J(THETA) is smallest, not growing


# 3-38 gradient descent in py
def compute_cost(features, values, theta):
    ''' compute cost fxn given 1) a set of features 2) set of values
    2) a theta value
    '''
    # get the length of Y, what were trying to predict
    m = len(values)

    # summ ( Xs * weight (of 1) - Ys ** 2)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()

    # just take that large num, divide by each and divide by 2
    cost = sum_of_square_errors / (2*m)
    return cost


def gradient_descent(features, values, theta, alpha, num_iterations):
    '''
    perform gradient descent given a data set w an arbitrary
    number of features
    '''
    # update the values of a theta a number of times
    
    # like last one, get length of all the Ys
    m = len(values)
    
    # set empty list, will add to it in each iteration
    cost_history = []

    # for each iteration    
    for i in range(num_iterations):
        # Ynu = Xs * theta or weight 
        predicted_values = np.dot(features, theta)
        
        # array with amt each prediction was off by
        residuals = predicted_values - values
        
        # residuals * all features for some reason
        # then multiply that by length of (Y) data
        # then alpha sound divide by this number
        # resulting number should be subtracted from the previous theta
        # previous theta is essentially the Yvalue when estimating model
        
        # small step in the direction of the steepest gradient
        theta = theta - alpha / m * np.dot(residuals, features)
        
        # this gets the sum of squared errors given the Xs, the Ys,
        # and our current value of theta, which is the Yestimator
        cost = compute_cost(features, values, theta)
        
        # append this cost to list of cost_historys
        cost_history.append(cost)
        
        # once finished for each iteration, return current/newest theta
        # and set of costs (each iteration)
        
    return theta, pd.Series(cost_history)

# read data in, isolate features and values
features = b2[['height', 'weight']]
values = b2['HR']
m = len(values)

## normalize the features - do not know what library this is from
import sklearn
#features, mu, sigma = normalize_features(features)

## would run above fxns, but no suggested/existing value of theta or alpha
#gradient_descent(features, values, theta, alpha, 10)

##3-40 - coefficient of determination or R**2
## data = yi...yn
# predictions = fi...fn
# avg of data = avg(y)
#r2 = 1 - sum(yi - fi)**2 / sum(yi-avg(y)**2)

#3-41 - coefficient of determination r2 in python
def compute_r_squared(data, predictions):
    ''' 
    arg1 is an array - the real ys
    arg2 is an array - the predicted ys
    output is R2 for the model that produced the predictions
    R2 ranges from 0-1
    '''
    total_sum_squares = sum((data - predictions)**2)
    sum_squares_regression = sum(data - np.mean(data)**2)
    r_sq = 1 - total_sum_squares / sum_squares_regression
    return r_sq
# apply it to our ys - HRs
# and our ypreds  - if any video had output that, would use



#3-43 - to use linear regression to solve real-world problem
# could use ordinary least squares regression
# always guarunteed to find optimal solution (gradient descent isnt)

# would want to also do
# parameter estimation and putting confidence intervals on those parameters

# what is the liklihood we would calculate this parameter value
# if the parameter had no effect?

# dont overfit
# model too complicated or
# train / test so dont overfit
# this is cross-validation

# underfitting
# putting a linear model on a non-linear X + real Y relationship

# cost fxn could have multiple local minima 
# (can disrupt gradient descent model)
# to solve
# can perform descent multiple times
#randomizing value of theta (starting pt) each time
# seed and store seed so result is repeatable

# stat model packages will give conf intervals


#3-44 - best practices
# qualitative - what do we know / what expectations, what to get
# dimensionality reduction - understand structure, intuition

# quantitative suggestion - understand which is x, which is y

# tips
# which of 3 parts enjoy
# 1-build code product 
# 2-analysis stats+math, ml techniques
# 3-communication, extract + present



#3-46 - assignment 3 - subway data
# use t-test - ride more in rain? on weekend?
#linear reg w gradient descent - most crowded day/time/weekday/weather etc



# 4-2 - info vizualization
# communicate complex quantitative ideas
# clarity, precision, efficiency

# highlight trends
# tell a story of it

## 4-3 - russia march
# flow line - width is size of army
# 2nd flow line is amt retreating after end
# 3rd line graph is temp

# depicts size of army, location, time, temp, 
# ez to understand why?
# ingredients like 
# visual cues, coordinate systems, scale / data types, context

# hrs by year
# 1-visual cue-pt is year, line is change
#2 - x is year, y is hrs
# 3 - scale - shows doubling/tripling
# numeric, categorical, time-series
# time is on x, numeric is on y
# 4 - context - pts like news events - steriods, 
# title, label axes, 



# 4-11 - visual encoding / cues
# 1-position x/y plot
# 2-length bar graph
# 3-angle pi chart

#4 - direction - single vectors orientation in coordinate system
# slight angles - hard

#5 - shape
# differentiate categories of objects
# such as in a scatterplot

#6 - area/volume of shapes
# larger circle, larger value

#7 - color
# hue - color rgb
# saturation - from light to dark version of that color
# combo light blue to dark red

# dont use more than 12 colors to differentiate b/w categories

# of these 4, best to worst in accuracy of visual encoding
# guessed
# area, saturation, position, angle

# answer
# position, angle, area, saturation



#4-17 - 
# 1985 att labels paper on graphical perception + methods
# position, length, angle, direction, area, volume, saturation, hue


#4-18 plotting in python
# ggplot instead of matplotlib cuz
# looks nice, implements grammar of graphics
# works well with dfs

# plots convey info thru aesthetics - xpos, ypos

# elements in plot are geometric shapes
# points, lines, bars
# these shapes can have a size or color or length

# step 1 - create plot or canvas
# data is a df, xvar and yvar are 2 columns in the df

### DOWNLOAD
#from ggplot import *

## scatterplot, connect them with lines
## add title, xlab, ylab
#ggplot(data, aes('xvar', 'yvar')) \
#  + geom_point(color="coral") + geom_line(color='coral') \
#          + ggtitle('title at top') \
#                   + xlab('x-label') + ylab('y label')


# 4-19 - do example of the above
#yearID and HR
def lineplot():
    '''
    assume have a csv titled hr_year.csv w cols yearID and HR
    creates a df then a chart with:
    - points connected by lines
    - both colored red
    - showing the name of HR by year
    '''
#    ggplot(hr_df, aes('yearID', 'HR')) \
#    + geom_point(color='red') + geom_line(color="red") \
#    + ggtitle('HR by year') \
#    + xlab('year') + ylab('HRs')



# 4-21 - data types
# most can be categorized into 3 types

# numeric
#quantitative - exact nums that can be a measurement or count
# discrete - whole number values
# continuous - nums that can fall in range .33333...

# categorical
# chars: position/team/town/handedness
# can be num, but cant add
# ordinal data
# categories with order/ranking like movie 1-5stars

# time-series data
# sequence of data collected via repeated measurements over time
# implies order



# 4-24 data scales
# categorical or ordinal
# barplot can use categorical on x axis, num on y axis

# time series
# days/months/years granularity on x-axis
# num on y-axis

# exs of bad scales
# 4% more but graph is 8x higher
# not linear or logorithmic scale


# plot line chart in py
def lineplot_compare():
    '''
    reads a csv called hr_by_team_year_sf_la.csv'
    it contains 3 cols:
    yearID, HR, teamID
    
    produce visual comparing total HR by year of the 2 teams.
    
    to differentiate b/w 2+ categories on the same plot in ggplot,
    pass in color in with other arguments (line) instead of shape
    aes(xvar, yvar, color=category_variable)
    '''
    ggplot(hr_by_team_year_sf_la, aes('yearID', 'HR', color='teamID')) \
    + geom_point() + geom_line() \
    + ggtitle('team HR by year') \
    + xlab('year') + ylab('team HRs')
    
# above doesnt specify a legend or choosing colors like their ex did



#4-29 - viz timeseries data
# nyc subway + weather data

# start with scatterplot, then like a loess curve?

# each dot shows a winning percentage, would be better with line connxn
# position - x,y
# context - label on x, on y, title

# line emphasizes trends
# focuses on year to year variability, not on overall/global trend

# might do a loess curve
# weighted regression
# captures overall trends rather than yr/yr effects



# 4-33: multivariate
# what is driving that winning percentage
# larger dots mean more HR, smaller when fewer HR
# can also make dark red for many HR, light red (cue) for few HR

# 4-37 recap
# compontents of effect viz
# visual cues, scale, position, context

# visual encoding
# size, position, color

# scales / data types
# num, cat, time-series

# creating graphics w gplot

# ridership at hours, how many ppl in/out stations



# 5 - mapreduce































