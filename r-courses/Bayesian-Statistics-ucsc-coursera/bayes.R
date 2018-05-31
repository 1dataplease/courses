### reading in lesson 1
# python range is same as r seq. doesnt start with 0 in r
l=seq(6); l

# range is only applied on lists
#it returns lowest and highest nums as list
l2 = range(l); l2

## 4-5 intro to r
x=6
expenses = x
expenses

z = c(2,3,4,5,6)
mean(Z)
var(z)
sd(z)
sqrt(var(z))

seq(from=1, to=9, by=1)

# dset built into r
trees
# get info - definitions - diameter,height,vol
help(trees)

# access datasets col labels
# can access them
# look into trees object for names and such
attach(trees)

names(trees)

## most have girth/diameter b/w 8 and 18 inches
hist(Girth)

## scatterplot - see height vs diameter
plot(Girth, Height)

## have all numerical cols plotted against each other
pairs(trees)

## get numerical summaries
summary(trees)



### 4-8 plot likelihood from hospital example
## can use binomial or a bernoulli likelihood. neither ~ theta
## simpler to stick w bernoulli, doesnt have terms

## likelihood ~ mortality rate theta
likelihood = function(n, deathes_y, theta){
  return( (theta^deathes_y) * (1-theta)^(n-deathes_y) )
}

## create a seq of events with mortality rates b/w 0 and 1
## plot likelihood values over that sequence
theta = seq(from=.01, to=.99, by=.01)

## plot theta by likelihood w n=400, y=72, theta
plot(theta, likelihood(400,72,theta))

## likelihood maximized at value 72/400
## add a line there
abline(v=.18)

## can do same w log likelihood - often easier and more stable to compute
loglike = function(n, deathes_y, theta){
  return(deathes_y*log(theta) + (n - deathes_y)*log(1 - theta))
}

## shows downward
plot(theta, loglike(400, 72, theta))

## plot the location with max again
abline(v=72/400)

## can add another argument - the type of plot: line now
plot(theta, loglike(400, 72, theta), type="l")


### 7-9 data analysis example
## binomial beta dists

# giving 2 students an exam with 40 questions, each w 4 choices
# 

