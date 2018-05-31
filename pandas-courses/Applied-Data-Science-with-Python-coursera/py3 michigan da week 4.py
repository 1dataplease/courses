import numpy as np
import pandas as pd
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
# not evenly weighted (tornados are rare)

#ask for a number
#np.random.binomial(# of simulations, likelihood of a 0)
np.random.binomial(1, 0.5)

#run simulation 1000x, divide result by 1000
np.random.binomial(1000, 0.5)/1000

#unevenly weighted binomial dist (tornado appearing)
#put it into a binomail distribution as a weighting
chance_of_tornado = .01 / 100

#out of 100,000 days only about 10 tornados
np.random.binomial(100000, chance_of_tornado)

#can quickly sim effects of parameters/args/factors 
#in a distribution

#whats chance of it 2 days in a row in 1,000,000 days
#this is called sampling the distribution

#new higher chance of tornado
chance_of_tornado = 1/100


#first get a list length 1,000,000, returns 0s, some 1s 
#create # of potential tornado events over 3k years
tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)

#right now there are 0 exs of tornados 2 days in row
two_days_in_a_row = 0

#for each day in range 0-end:
#   if its a 1 and the one before was a 1:
#       add 1 to two_days_in_row
for day in range(1, len(tornado_events)-1):
    if tornado_events[day] == 1 and tornado_events[day-1] == 1:
        two_days_in_a_row += 1

#can do print 'sdfs{} seer{}'.format(var1, var2)
print('{} tornadoes back2back in {} years'\
      .format(two_days_in_a_row, 1000000/365))

#4-3
#more distributions

#4-2 was discrete binomial dist

#many are continuous - can be represented as #
#   graphing them, x=value, y=prob.
#       if equally likely, graphed as thick line
#           uniform distribution

#normal / gaussian distribution
#mean is 0
#2 curves symetric, 95% of values within 2 stdevs

#expected value is the probability of most likely VALUE

#variance is measure of how broadly the samples are spread from mean

#central tendency - mode, median, mean
# where bulk of probability is

#variability in dist: stdev, interquartile range

#formula for stdev

#draw 1000 samples from normal dist, expected val = .75, stdev=1
dist = np.random.normal(.75, size=1000)

#1. calculate the actual mean of dist
np.mean(dist)
#2. calculate difference b/w that and each point
np.mean(dist) - dist
#3. take the difference, square it
(np.mean(dist) - dist)**2
#4. add up all the squares up
(np.sum(np.mean(dist) - dist)**2)
#5. srqrt that sum
np.sqrt(np.sum(np.mean(dist) - dist)**2)
#6. divide it by the # in the distribution
np.sqrt(np.sum(np.mean(dist) - dist)**2)/len(dist)

#thats the size of the stdev, covers 68% around mean, even
np.std(dist)

# more measures of dist
#shape of the tail of the distribution - kurtosis
#negative - more flat
#positive - fatter tail

import scipy.stats as stats
stats.kurtosis(dist)

#not measuring kurtosis of dist, but measuring kurtosis
# of the 1000 values we sampled out of the distribution

#skew
#could push peak left or right
stats.skew(dist)

## chi-squared distribution
#is left-skewed in liklihood

#degrees of freedom = 4
#df is closely related 2 number of samples u take from normal
#as degreeFreedom up, skews closer to the center normal dist

#skew to left starts moving to center

#sample 1000 values from chi-sq dist w/ df=2
chi_squared_df2 = np.random.chisquare(2, size=10000)
#see what the skew is, large 2.14
stats.skew(chi_squared_df2)

#resample it with df=5
chi_squared_df5 = np.random.chisquare(5, size=10000)
#now skew is smaller, 1.31
stats.skew(chi_squared_df5)

#plot this - histogram
#shows distributions and shows skew
import matplotlib.pyplot as plt

output = plt.hist([chi_squared_df2, chi_squared_df5],
                  bins=50, histtype='step',
                  label=['2 degrees freedom', '5 degrees freedom'])
plt.legend(loc='upper right')

#modality
#so far all these dists have a single high-point
#some can have multiple 

#can model these using 2 normal distributions w diff parameters

#dist is a 
#shape that describes probability of value being sampled

#numpy and scipy have some built in for samples

#free book - think stats


#4-4
#hypothesis testing

#experimentation, change factor a/b, see how they output

#ethics - reading

#hypothesis is a stmt we can test
#alternative hypothesis: new idea, diff b/w groups
#null hypothesis: there is NO diff b/w groups

#quick sign-ups perform higher than slow sign-ups
#take sample of earlybirds, latebirds

#alt: diff
#null: no diff

#evidence against no diff

# id, 6 assignments, each w grade and random submission time
df = pd.read_csv('grades.csv')
df.head()

#segment into earlys and lates - each roughly same size
early = df[df['assignment1_submission'] <= '2015-12-31' ]
late = df[df['assignment1_submission'] > '2015-12-31' ]

#find on the number cols - there is diff of .95 score
early.mean()
late.mean()

#critical value alpha
#the threshod as to how much chance we're willing to accept
#.05, .01
#in physics - 10^-5

from scipy import stats
#compare 2 independent samples to see if mean_diff is StatSig
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade'])
stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade'])
#returns (test_statistic, p-value)
#p-value is .16, not enough diff

#stop and talk about process problem
#when you set alpha .05. 1/20 + by chance

#if you run a lot of tests, p-hacking/dredging
#results in spurrious results


#1 correction - bonferroni correction
#tighten the alpha based on # of tests youre running
#.05 * 1/3 = .017
#possibly too conservative

#2 correction - hold-out some of data for testing
#               cross-fold validation
#cut original df in half, run t-tests on our samples
#run limited tests on the original half we left out

#3 - preregister experiment w/ 3rd party
#run story, report results

#course2 is plotting/charting/story