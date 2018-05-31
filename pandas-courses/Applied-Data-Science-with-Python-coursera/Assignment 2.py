#to do this, open assignment2.ipy by doing
#ipython notebook


# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 2 - Pandas Introduction
# All questions are weighted the same in this assignment.
# ## Part 1
# The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry on [All Time Olympic Games Medals](https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table), and does some basic data cleaning. 
# 
# The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals, total # number of games, total # of medals. Use this dataset to answer the questions below.

# In[1]:

import pandas as pd

#i input
import os
os.chdir('C:\\Users\\wainman\\Desktop\\tw\\classes\\1 python michigan data-analysis\\course1_downloads')

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]== '№':
        df.rename(columns={col:'num'+col[1:]}, inplace=True)

# split the index (country name) by '('
names_ids = df.index.str.split('\(') 
#names_ids = df.index.str.split('\s\(') 
#names_ids = names_ids.str.split("'\s\('") 
names_ids

# the [0] element is the country name (new index) 
bla = names_ids.str[0]
#did this to take out the space at the end my split didnt get
bla = bla.str[:-2]
df.index = bla

# the [1] element is the abbreviation or ID (take first 3 characters from that)
df['ID'] = names_ids.str[1].str[:3]

#this drops totals column. i renamed it tota above
df = df.drop('Tota')
df.head()

# ### Question 0 (Example)
# 
# What is the first country in df?
# 
# *This function should return a Series.*

# In[ ]:

# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 


# ### Question 1
# Which country has won the most gold medals in summer games?
# 
# *This function should return a single string value.*

# In[ ]:

#finds the index with the largest in column
#df.col.idxmax()

def answer_one():
    return df.Gold.idxmax()

answer_one()

# ### Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
# 
# *This function should return a single string value.*

# In[ ]:

#finds the one index with largest diff bw columns
#df.1 - df.2.idxmax()

def answer_two():
    return (df.Gold - df['Gold.1']).idxmax()
answer_two()

# ### Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count? 
# 
# $$\frac{Summer~Gold - Winter~Gold}{Total~Gold}$$
# 
# Only include countries that have won at least 1 gold in both summer and winter.
# 
# *This function should return a single string value.*

# In[ ]:



def answer_three():
    return ((df.Gold - df['Gold.1'])/df['Gold.2']).idxmax()
answer_three()

# ### Question 4
# Write a function that creates a Series called "Points" which is a weighted value 
#where each gold medal (`Gold.2`) counts for 3 points, 
#silver medals (`Silver.2`) for 2 points, and 
#bronze medals (`Bronze.2`) for 1 point. 
#The function should return only the column (a Series object) 
#which you created.
# 
# *This function should return a Series named `Points` of length 146*

# In[ ]:

def answer_four():
    df['Points'] = 3*df['Gold.2'] + 2*df['Silver.2'] + df['Bronze.2']
    return df['Points']
answer_four()
# ## Part 2
# For the next set of questions, we will be using census data from the [United States Census Bureau](http://www.census.gov/popest/data/counties/totals/2015/CO-EST2015-alldata.html). Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. [See this document](http://www.census.gov/popest/data/counties/totals/2015/files/CO-EST2015-alldata.pdf) for a description of the variable names.
# 
# The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.
# 
# ### Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# 
# *This function should return a single string value.*

# In[ ]:

census_df = pd.read_csv('census.csv')
census_df.head()


# In[ ]:

#which st has most counties in it
#df.groupby('col')['col'].count().idxmax()

def answer_five():
    by_state = census_df.groupby('STNAME')
    return by_state['CTYNAME'].count().idxmax()
answer_five()


# ### Question 6
#Only looking at the three most populous counties for each state
#what are the three most populous states 
#(in order of highest population to lowest population)? 
#Use `CENSUS2010POP`.
# 
# *This function should return a list of string values.*

# In[ ]:

census_df = pd.read_csv('census.csv')
census_df.head()
counties = census_df[census_df['SUMLEV'] == 50]


# sort_values([BY STATE, THEN BY POP]), ascending=[1,0])
ordered = counties.sort(['STNAME', 'CENSUS2010POP'], ascending=[1,0]).reset_index()

#groupby state so we can take 3 best from it
grouped = ordered.groupby('STNAME')

#this takes the top3 OF EACH STATE, but its a df
grouped.head(3)

#turn df back into a groupby object of the state
top3 = grouped.head(3).groupby('STNAME')

#get sum of top3 of states
import numpy as np
top3.agg({'CENSUS2010POP': np.sum})

#now sort the top3_added_together
sorted_answer = top3.agg({'CENSUS2010POP': np.sum}).sort('CENSUS2010POP', ascending=False)

#now get it into string
list(sorted_answer['CENSUS2010POP'].nlargest(3).index)

def answer_six():
    counties = census_df[census_df['SUMLEV'] == 50]
    ordered = counties.sort(['STNAME', 'CENSUS2010POP'], ascending=[1,0]).reset_index()
    grouped = ordered.groupby('STNAME')
    top3 = grouped.head(3).groupby('STNAME')
    top3.agg({'CENSUS2010POP': np.sum})
    sorted_answer = top3.agg({'CENSUS2010POP': np.sum}).sort('CENSUS2010POP', ascending=False)
    return list(sorted_answer['CENSUS2010POP'].nlargest(3).index)
answer_six()


# ### Question 7
# Which county has had the largest absolute change in population 
#within the period 2010-2015? 
#(Hint: population values are stored in columns 
#POPESTIMATE2010 through POPESTIMATE2015
#you need to consider all six columns.)
# 
# e.g. If County Population in the 5 year period is 
#100, 120, 80, 105, 100, 130, then its largest change in the period 
#would be |130-80| = 50.
# 
# *This function should return a single string value.*

# In[ ]:

counties = census_df[census_df['SUMLEV'] == 50]
keep = ['CTYNAME', 'POPESTIMATE2010', 'POPESTIMATE2011','POPESTIMATE2012',\
'POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015'] 
import numpy as np

#just counties and just population columns
county_pop = counties[keep]

#id by CTYNAME
county_pop = county_pop.set_index('CTYNAME')

abs_changes = county_pop.apply(lambda x: abs(np.max(x) - np.min(x)), axis=1)

abs_changes.idxmax()

def answer_seven():
    counties = census_df[census_df['SUMLEV'] == 50]
    keep = ['CTYNAME', 'POPESTIMATE2010', 'POPESTIMATE2011','POPESTIMATE2012',\
    'POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
    county_pop = counties[keep]
    county_pop = county_pop.set_index('CTYNAME')
    #do calc
    abs_changes = county_pop.apply(lambda x: abs(np.max(x) - np.min(x)), axis=1)
    return abs_changes.idxmax()
answer_seven()

# ### Question 8
# In this datafile, the United States is broken up into four regions 
#using the "REGION" column. 
# 
# Create a query that finds the counties that belong 
#to regions 1 or 2
#whose name starts with 'Washington'
#and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
# 
# *This function should return a 5x2 DataFrame with the 
#columns = ['STNAME', 'CTYNAME'] 
#and the same index ID as the census_df (sorted ascending by index).*

# In[ ]:

keep = ['STNAME', 'CTYNAME', 'REGION', 'POPESTIMATE2014','POPESTIMATE2015']
county_region = counties[keep]
#county_region = county_region.set_index(['STNAME', 'CTYNAME'])

ans = county_region.loc[(county_region['CTYNAME'].str.startswith('Washington')) \
& (county_region['REGION'] < 3) \
& (county_region['POPESTIMATE2015'] > county_region['POPESTIMATE2014'])]

keep_only_2 = ['STNAME', 'CTYNAME']
ans = ans[keep_only_2]

def answer_eight():
    counties = census_df[census_df['SUMLEV'] == 50]
    keep = ['STNAME', 'CTYNAME', 'REGION', 'POPESTIMATE2014','POPESTIMATE2015']
    county_region = counties[keep]
    #county_region = county_region.set_index(['STNAME', 'CTYNAME'])
    
    ans = county_region.loc[(county_region['CTYNAME'].str.startswith('Washington')) \
    & (county_region['REGION'] < 3) \
    & (county_region['POPESTIMATE2015'] > county_region['POPESTIMATE2014'])]
    
    keep_only_2 = ['STNAME', 'CTYNAME']
    ans = ans[keep_only_2]
    return ans

answer_eight()