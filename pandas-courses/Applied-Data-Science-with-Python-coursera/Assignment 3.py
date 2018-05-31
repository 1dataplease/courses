# coding: utf-8
#**version 1.5** of this notebook. To download notebooks and df

#[Jupyter Notebook FAQ]
#(https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# ---

# # Assignment 3 - More Pandas
#http://pandas.pydata.org/pandas-docs/stable/ 
#to find functions or methods you might not have used yet, 


# ### Question 1 (20%)
# Load the energy data from the file `Energy Indicators.xls`, 
#http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls
#put into a DataFrame with the 
#variable name of **energy**.

#0. xlsx not csv
#1. exclude the footer and header from df ,drop first 2 cols
#2. change the column labels so that the columns are:
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']`
# 
#3. Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule)
#4. For all countries w missing data (e.g. data with "...") import as `np.NaN`
# 
#5. Rename the following list of countries (for use in later questions):
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# 
#6. There are also several countries with numbers and/or parenthesis in their name. 
#Be sure to remove these, 
# `'Bolivia (Plurinational State of)'` should be `'Bolivia'`, 
# `'Switzerland17'` should be `'Switzerland'`.

#7.  load the GDP data from the file `world_bank.csv`
#a csv containing countries' GDP from 1960 to 2015 from [World Bank]
#http://data.worldbank.org/indicator/NY.GDP.MKTP.CD)
#7b. Call this DataFrame **GDP**. 

#8.  Make sure to skip the header, and rename the following list of countries:
# ```"Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```

#9. Finally, load the [Sciamgo data for Energy Engineering and Power Technology]
#http://www.scimagojr.com/countryrank.php?category=2102 from the file `scimagojr-3.xlsx`
#ranks countries based on their journal contributions in energy. 
#9b. Call this DataFrame **ScimEn**.

#10. Join the three datasets: GDP, Energy, and ScimEn into a new dataset 
#10b. (using the intersection of country names). 
#10c. Use only the last 10 years (2006-2015) of GDP data and 
#10d. only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15). 
# 
#10e. The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# 
# *This function should return a DataFrame with 20 columns and 15 entries.*

# In[ ]:
import os
import pandas as pd
import numpy as np
os.chdir('C:\\Users\\wainman\\Desktop\\tw\\classes\\1 python michigan data-analysis\\course1_downloads')

energy0 = pd.read_excel('Energy Indicators.xls', index=False)
energy = energy0.drop(range(16))
energy.drop(['Unnamed: 0', 'Unnamed: 1'], inplace=True, axis=1)
energy.drop(range(243,len(energy0)), inplace=True)

#set dropped indexs back, remove the original index that came back also
energy.reset_index(inplace=True)
energy.drop(['index'], axis=1, inplace=True)

keep= ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
energy.columns = keep

#convert pJ to gJ
energy['Energy Supply'] = energy['Energy Supply'] * 1000000
energy['Energy Supply per Capita'] = energy['Energy Supply per Capita'] * 1000000

#convert all '...' data to np.nan
energy['Energy Supply'] = energy['Energy Supply'].convert_objects(convert_numeric=True)
energy['Energy Supply per Capita'] = energy['Energy Supply per Capita'].convert_objects(convert_numeric=True)
energy

#rename countries
energy['Country'] = energy['Country'].str.replace(r'[0-9]', '')
energy['Country'] = energy['Country'].str.replace(r' \(.*\)', '')

energy['Country'] = energy['Country'].str.replace("Republic of Korea", "South Korea")
energy['Country'] = energy['Country'].str.replace("United States of America", "United States")
energy['Country'] = energy['Country'].str.replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")
energy['Country'] = energy['Country'].str.replace("China, Hong Kong Special Administrative Region", "Hong Kong")

#first 3 rows are blank, 4th has the column names. also drop any lines that are all na
GDP = pd.read_csv('world_bank.csv', skiprows=3, header=True)
GDP.dropna(how="all", inplace=True)

#rename country values
GDP['Country Name'] = GDP['Country Name'].str.replace("Korea, Rep.", "South Korea")
GDP['Country Name'] = GDP['Country Name'].str.replace("Iran, Islamic Rep.", "Iran")
GDP['Country Name'] = GDP['Country Name'].str.replace("Hong Kong SAR, China", "Hong Kong")

#last df - schiago w Country
ScimEn = pd.read_excel('scimagojr-3.xlsx')

#10. Join the three datasets: GDP, Energy, and ScimEn into a new dataset 
#10b. (using the intersection of country names)
#gives a weird message saying it didnt convert them as unicode, interpreted unequal
other2 = pd.merge(energy, GDP, how='left', left_on="Country", right_on="Country Name")
df = pd.merge(ScimEn, other2, how='left', left_on="Country", right_on="Country")

#10c. Use only the last 10 years (2006-2015) of GDP data and 
#10d. only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
keep = ['Country', 'Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',\
'Citations per document', 'H index', 'Energy Supply',\
'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',\
'2009', '2010', '2011', '2012', '2013', '2014', '2015']
df = df[keep]

#drop non-top-15 countries
df.drop(range(15,len(df)), inplace=True)
df.set_index('Country', inplace=True)


def answer_one():
    energy0 = pd.read_excel('Energy Indicators.xls', index=False)
    energy = energy0.drop(range(16))
    energy.drop(['Unnamed: 0', 'Unnamed: 1'], inplace=True, axis=1)
    energy.drop(range(243,len(energy0)), inplace=True)
    
    #set dropped indexs back, remove the original index that came back also
    energy.reset_index(inplace=True)
    energy.drop(['index'], axis=1, inplace=True)
    
    keep= ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.columns = keep
    
    #convert pJ to gJ
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    energy['Energy Supply per Capita'] = energy['Energy Supply per Capita'] * 1000000
    
    #convert all '...' data to np.nan
    energy['Energy Supply'] = energy['Energy Supply'].convert_objects(convert_numeric=True)
    energy['Energy Supply per Capita'] = energy['Energy Supply per Capita'].convert_objects(convert_numeric=True)
    energy
    
    #rename countries
    energy['Country'] = energy['Country'].str.replace(r'[0-9]', '')
    energy['Country'] = energy['Country'].str.replace(r' \(.*\)', '')
    
    energy['Country'] = energy['Country'].str.replace("Republic of Korea", "South Korea")
    energy['Country'] = energy['Country'].str.replace("United States of America", "United States")
    energy['Country'] = energy['Country'].str.replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")
    energy['Country'] = energy['Country'].str.replace("China, Hong Kong Special Administrative Region", "Hong Kong")
    
    #first 3 rows are blank, 4th has the column names. also drop any lines that are all na
    GDP = pd.read_csv('world_bank.csv', skiprows=3, header=True)
    GDP.dropna(how="all", inplace=True)
    
    #rename country values
    GDP['Country Name'] = GDP['Country Name'].str.replace("Korea, Rep.", "South Korea")
    GDP['Country Name'] = GDP['Country Name'].str.replace("Iran, Islamic Rep.", "Iran")
    GDP['Country Name'] = GDP['Country Name'].str.replace("Hong Kong SAR, China", "Hong Kong")
    
    #last df - schiago w Country
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    
    #10. Join the three datasets: GDP, Energy, and ScimEn into a new dataset 
    #10b. (using the intersection of country names)
    #gives a weird message saying it didnt convert them as unicode, interpreted unequal
    other2 = pd.merge(energy, GDP, how='left', left_on="Country", right_on="Country Name")
    df = pd.merge(ScimEn, other2, how='left', left_on="Country", right_on="Country")
    
    #10c. Use only the last 10 years (2006-2015) of GDP data and 
    #10d. only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
    keep = ['Country', 'Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',\
    'Citations per document', 'H index', 'Energy Supply',\
    'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',\
    '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    df = df[keep]
    
    #drop non-top-15 countries
    df.drop(range(15,len(df)), inplace=True)
    df.set_index('Country', inplace=True)

    return df
answer_one()

# ### Question 2 (6.6%)
# The previous question joined three datasets then reduced this to just the top 15 entries. 
#When you joined the datasets, but before you reduced this to the top 15 items
#how many entries did you lose?
# 
# *This function should return a single number.*

# In[1]:

get_ipython().run_cell_magic(u'HTML', u'', u'<svg width="800" height="300">\n  <circle cx="150" \cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


# In[ ]:

def answer_two():
    energy0 = pd.read_excel('Energy Indicators.xls', index=False)
    energy = energy0.drop(range(16))
    energy.drop(['Unnamed: 0', 'Unnamed: 1'], inplace=True, axis=1)
    energy.drop(range(243,len(energy0)), inplace=True)
    
    #set dropped indexs back, remove the original index that came back also
    energy.reset_index(inplace=True)
    energy.drop(['index'], axis=1, inplace=True)
    
    keep= ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.columns = keep
    
    #convert pJ to gJ
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    energy['Energy Supply per Capita'] = energy['Energy Supply per Capita'] * 1000000
    
    #convert all '...' data to np.nan
    energy['Energy Supply'] = energy['Energy Supply'].convert_objects(convert_numeric=True)
    energy['Energy Supply per Capita'] = energy['Energy Supply per Capita'].convert_objects(convert_numeric=True)
    energy
    
    #rename countries
    energy['Country'] = energy['Country'].str.replace(r'[0-9]', '')
    energy['Country'] = energy['Country'].str.replace(r' \(.*\)', '')
    
    energy['Country'] = energy['Country'].str.replace("Republic of Korea", "South Korea")
    energy['Country'] = energy['Country'].str.replace("United States of America", "United States")
    energy['Country'] = energy['Country'].str.replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")
    energy['Country'] = energy['Country'].str.replace("China, Hong Kong Special Administrative Region", "Hong Kong")
    
    #first 3 rows are blank, 4th has the column names. also drop any lines that are all na
    GDP = pd.read_csv('world_bank.csv', skiprows=3, header=True)
    GDP.dropna(how="all", inplace=True)
    
    #rename country values
    GDP['Country Name'] = GDP['Country Name'].str.replace("Korea, Rep.", "South Korea")
    GDP['Country Name'] = GDP['Country Name'].str.replace("Iran, Islamic Rep.", "Iran")
    GDP['Country Name'] = GDP['Country Name'].str.replace("Hong Kong SAR, China", "Hong Kong")
    
    #last df - schiago w Country
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    
    #10. Join the three datasets: GDP, Energy, and ScimEn into a new dataset 
    #10b. (using the intersection of country names)
    #gives a weird message saying it didnt convert them as unicode, interpreted unequal
    other2 = pd.merge(energy, GDP, how='left', left_on="Country", right_on="Country Name")
    df = pd.merge(ScimEn, other2, how='left', left_on="Country", right_on="Country")
    
    #10c. Use only the last 10 years (2006-2015) of GDP data and 
    #10d. only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
    keep = ['Country', 'Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',\
    'Citations per document', 'H index', 'Energy Supply',\
    'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',\
    '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    df = df[keep]
    return len(df)
answer_two()

# <br>
# 
# Answer the following questions for only the top 15 countries by Scimagojr Rank 
#(aka the DataFrame returned by `answer_one()`)

# ### Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? 
#(exclude missing values from this calculation.)
# 
# *This function should return a Series named `avgGDP` with 15 countries 
#AND their average GDP sorted in descending order.*

# In[ ]:
years0 = ["2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006"]
years = df[years0]
avgGDP = years.sum(axis=1)/years.count(axis=1)
avgGDP.sort(ascending=False)

def answer_three():
    Top15 = answer_one()
    years0 = ["2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006"]
    years = Top15[years0]
    avgGDP = years.sum(axis=1)/years.count(axis=1)
    avgGDP.sort(ascending=False)
    return avgGDP
answer_three()

# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span 
#for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[ ]:



def answer_four():
    Top15 = answer_one()
    uk_gdp_change = df.loc['United Kingdom', '2015'] - df.loc['United Kingdom', '2006']
    return uk_gdp_change
answer_four()

# ### Question 5 (6.6%)
# What is the mean `Energy Supply per Capita`?
# 
# *This function should return a single number.*

# In[ ]:

df['Energy Supply per Capita'].mean()

def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()
answer_five()

# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[ ]:
(df['% Renewable'].idxmax(), df.loc[df['% Renewable'].idxmax()]['% Renewable'])


def answer_six():
    Top15 = answer_one()
    return (Top15['% Renewable'].idxmax(), Top15.loc[Top15['% Renewable'].idxmax()]['% Renewable'])
answer_six()

# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[ ]:
df['self_cite_pct'] = df['Self-citations'] / df['Citations']
(df['self_cite_pct'].idxmax(), df.loc[df['self_cite_pct'].idxmax()]['self_cite_pct'])

def answer_seven():
    Top15 = answer_one()
    Top15['self_cite_pct'] = Top15['Self-citations'] / Top15['Citations']
    return (Top15['self_cite_pct'].idxmax(), Top15.loc[Top15['self_cite_pct'].idxmax()]['self_cite_pct'])
answer_seven()


# ### Question 8 (6.6%)
# 
# Create a column that estimates the populn using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return a single string value.*

# In[ ]:

#corr bw population and energy supply, then b/w energy supply per capita?
df['pop'] = 100000000000*(df['Energy Supply per Capita'] / df['Energy Supply'])

#3rd most populated WHAT
bla = df['pop'].copy()
bla.sort()
bla[2]

#not used yet
df['pop'].corr(df['Energy Supply'])
df['pop'].corr(df['Energy Supply per Capita'])

#

def answer_eight():
    Top15 = answer_one()
    Top15['pop'] = 100000000000*(Top15['Energy Supply per Capita'] / df['Energy Supply'])
    bla = df['pop'].copy()
    bla.sort()
    return bla[2]
answer_eight()

# ### Question 9 (6.6%)
# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and 
#the energy supply per capita? 
#Use the `.corr()` method, (Pearson's correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[ ]:

df['citable_docs_per_capita'] = df['Citations']/df['pop']
df['citable_docs_per_capita'].corr(df['Energy Supply'])
#plot9(df['citable_docs_per_capita'], df['Energy Supply'])

def answer_nine():
    Top15 = answer_one()
    Top15['citable_docs_per_capita'] = Top15['Citations']/Top15['pop']
    return Top15['citable_docs_per_capita'].corr(Top15['Energy Supply'])


# In[ ]:

def plot9():
    import matplotlib as plt
    get_ipython().magic(u'matplotlib inline')
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
plot9()

# In[ ]:

#plot9() # Be sure to comment out plot9() before submitting the assignment!


# ### Question 10 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median 
#and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name 
#sorted in ascending order of rank.*

# In[ ]:
#def med(item):
#    if item < np.median(item):
#        return 0
#    elif item > np.median(item):
#        return 1

df.ix[df['% Renewable'] >= np.median(df['% Renewable']), 'HighRenew'] = 1
df.ix[df['% Renewable'] < np.median(df['% Renewable']), 'HighRenew'] = 0 
df['HighRenew']

def answer_ten():
    Top15 = answer_one()
    Top15.ix[Top15['% Renewable'] >= np.median(Top15['% Renewable']), 'HighRenew'] = 1
    Top15.ix[Top15['% Renewable'] < np.median(Top15['% Renewable']), 'HighRenew'] = 0 
    return Top15['HighRenew']


# ### Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, 
#then create a dateframe that displays the sample size (the number of countries in each continent bin), 
#and the sum, mean, and std deviation for the estimated population of each country.
# 

ContinentDict  = {'China':'Asia', 
                   'United States':'North America', 
                   'Japan':'Asia', 
                   'United Kingdom':'Europe', 
                   'Russian Federation':'Europe', 
                   'Canada':'North America', 
                   'Germany':'Europe', 
                   'India':'Asia',
                   'France':'Europe', 
                   'South Korea':'Asia', 
                   'Italy':'Europe', 
                   'Spain':'Europe', 
                   'Iran':'Asia',
                   'Australia':'Australia', 
                   'Brazil':'South America'}



ser = pd.Series(ContinentDict)
df['cont'] = ser

contCount = df.groupby('cont')['cont'].count()
contExtra = df.groupby('cont')['pop'].agg({np.std, np.mean, np.sum})

#insert Count as first column of contExtra
continents = pd.concat([contCount, contExtra], axis=1)
continents.columns = ['size', 'sum', 'mean', 'std']

# *This function should return a DataFrame with 
#index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and 
#columns `['size', 'sum', 'mean', 'std']`*

# In[ ]:

def answer_eleven():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                       'United States':'North America', 
                       'Japan':'Asia', 
                       'United Kingdom':'Europe', 
                       'Russian Federation':'Europe', 
                       'Canada':'North America', 
                       'Germany':'Europe', 
                       'India':'Asia',
                       'France':'Europe', 
                       'South Korea':'Asia', 
                       'Italy':'Europe', 
                       'Spain':'Europe', 
                       'Iran':'Asia',
                       'Australia':'Australia', 
                       'Brazil':'South America'}
    Top15['cont'] = pd.Series(ContinentDict)
    contCount = Top15.groupby('cont')['cont'].count()
    contExtra = Top15.groupby('cont')['pop'].agg({np.std, np.mean, np.sum})
    
    #insert Count as first column of contExtra
    continents = pd.concat([contCount, contExtra], axis=1)
    continents.columns = ['size', 'sum', 'mean', 'std']
    return continents


# ### Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, 
#as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a __Series__ with a MultiIndex of `Continent`, 
#then the bins for `% Renewable`. Do not include groups with no countries.*

# In[ ]:

def answer_twelve():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# 
# e.g. 317615384.61538464 -> 317,615,384.61538464
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[ ]:

def answer_thirteen():
    Top15 = answer_one()
    return "ANSWER"


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[ ]:

def plot_optional():
    import matplotlib as plt
    get_ipython().magic(u'matplotlib inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")


# In[ ]:

#plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!

