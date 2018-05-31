setwd('C:/Users/wainman/Desktop/tw/classes/7 DA with R')
getwd()

#2-10
x = c(0:10, 50); x
xm = mean(x); xm
c(xm, mean(x, trim = .3))
mean(x[2:11])
?mean

#2-11
#read and subset
statesInfo = read.csv('stateData.csv')
statesInfo2 = read.csv('statesinfo.csv')

stateSubset = subset(statesInfo, state.region == 1)
# stateSubsetBracket = statesInfo[statesInfo$state.region == 1, ]

head(stateSubset)
dim(stateSubset)


#2-12
#cars and r markdown
subset(mtcars, mpg > 30 | hp < 60)
mtcars[mtcars$mpg>30 | mtcars$hp < 60, ]


#2-14
#reddit questions
getwd()
reddit = read.csv('reddit.csv')
table(reddit$employment.status)
summary(reddit)

#2-15
str(reddit)
#age.range is a factor with 7 levels
levels(reddit$age.range)
library(ggplot2)
qplot(data= reddit, x = age.range)

#2-16
#want to change order so under-18 on left
##non-factors / non-binary can be converted to an ORDERED factor

#2-17
qplot(data= reddit, x = income.range)

#2-18
### solution
reddit$age.range <- ordered(reddit$age.range, 
                            levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", 
                                       "55-64", "65 or Above"))

levels(reddit$income.range)

reddit$income.range <- ordered(reddit$income.range, 
                               levels = c("Under $20,000", "$20,000 - $29,999", "$30,000 - $39,999", "$40,000 - $49,999", "$50,000 - $69,999", "$70,000 - $99,999", "$100,000 - $149,999","$150,000 or more" ))

#2-19
#these are tidy datasets - rows columns (lesson 5 is munging)
#data munging course

#3-1
##single variable in dataset - boxplot, scatterplot

#3-3
list.files()
fb <- read.csv('pseudo_facebook.tsv', sep = '\t') #not real
names(fb)

#3-4
#look at birthdays using ggplot
library(ggplot2)
qplot(data=fb, x=dob_day)

# binwidth defaulted to range/30. to correct:

#see every day on x-axis
qplot(data=fb, x=dob_day) +
  scale_x_continuous(breaks=1:31)

#3-6
#estimate audience size
#does who sees your post == survey_how_many_ppl_saw_your_post
#sports post, 30, 10%
#really higher
##ggplot - histogram of ppls guesses

#3-9
#plot out histogram of ppls birthdays
```{r}
qplot(data=fb, x=dob_day) +
  scale_x_discrete(breaks=1:31) +
  facet_wrap(~dob_month, ncol=4)
```
#create the same plot for each type of categorical variable
#facet_wrap(~variable)
#histograms for dob-day, one for each month

#faceting over 2+ variables
#facet_grid(vertical ~ horizontal)

#3-13
#ex - income info - replaced with other value
#adjust axis, get rid of 1mil - range 0-1200
#bad data about an extreme case
#adjust/replace/exclude

#3-14
#histogram of friend counts
names(fb)
head(fb$friend_count)
qplot(data=fb, x=friend_count)

#want to make the axis smaller
qplot(data=fb, x=friend_count, xlim=c(0,1000))

```{r}
qplot(data=fb, x=friend_count) +
  scale_x_continuous(limits = c(0,1000))
```

#3-17, 3-18
#adjust binwidth
#1 - shows the numbers in 10s or 50s
#without breaks, only shows labels at 250
#binwidth clumps them together
```{r}
qplot(data=fb, x=friend_count, binwidth=25) +
  scale_x_continuous(limits = c(0,1000), breaks = seq(0,1000,50))
```

#3-19
#friends by gender
#2 hist - m/f/na

#3-20
#facet wrap, get rid of na w/ subset
```{r}
qplot(x=friend_count,data=subset(fb, !is.na(gender)), binwidth=25)+
  scale_x_continuous(limits = c(0,1000), breaks = seq(0,1000,50)) +
  facet_wrap(~gender)
```

#could also do na.omit
#be careful, it will omit users with na in other columns
```{r}
qplot(x=friend_count, data=na.omit(fb), binwidth=25) +
  scale_x_continuous(limits = c(0,1000), breaks = seq(0,1000,50)) +
  facet_wrap(~gender)
```


#3-21, 3-22
#gives # of m/f
table(fb$gender)

#look at average friend count by gender
# by(variable we run fxn on, cat-variable to group, fxn we run)
#summ gives mean,med,min,max,qtr
by(fb$friend_count, fb$gender, summary)

#median more robust, representative not dragged by outliers
#long tail so mean is larger
#as long as we trust 1/2 of values, can report center of dist

#3-23
#tenure - days using fb
#color + fill
qplot(x=tenure, data=fb,
      color = I('black'), fill = I('#099DD9'))

#3-24
#tenure number of years, not days, also add labels, small bins
#3-25
#cont x scale 1-7, breaks 0-7
```{r}
qplot(x=tenure/365, data=fb, binwidth=.25,
      xlab = 'Number of years using fb',
      ylab = 'Number of users in sample',
      color = I('black'), fill = I('#099DD9')) +
  scale_x_continuous(breaks = seq(1,7,1), lim=c(0,7))
```


#3-26
#make histogram of users by age
#binwidth, breaks and labels
qplot(data=fb, x=age) #too long a tail
qplot(data=fb, x=age, binwidth=5) #thicker bin but tail still
```{r}
qplot(data=fb, x=age, binwidth=5,
      xlab = 'age',
      ylab='# of users in sample') +
  scale_x_continuous(breaks=seq(15,70,5), lim=c(14,70))

```

#3-27
#binwidth 1 lets us see spikes at 100,25,etc
#seq can be 0, til max of 113. limit i added
```{r}
qplot(data=fb, x=age, binwidth=1,
      xlab = 'age',
      ylab='# of users in sample') +
  scale_x_continuous(breaks=seq(0,113,5), lim=c(13,75))
```

#3-29
#how did the moneybags meme comeback
#longer weeks or something

#3-30
#transforming variables - engagement variables w/ long tails
#data is overdispersed, see sds
#lots of regressions can be used once data made more normal
qplot(x=friend_count, data=fb)
summary(fb$friend_count)

#10-fold scale like ph
summary(log10(fb$friend_count + 1)) #so we dont get -inf
qplot(x=log10(fb$friend_count + 1))

#do hist of these 2 - sqrts of friends
summary(sqrt(fb$friend_count))
qplot(x=sqrt(fb$friend_count))

#3-31 - all 3 on 1 plot
library(gridExtra)

#method 1: wrapper around variable
p1 = qplot(x=friend_count, data=fb)
p2= qplot(x=log10(friend_count + 1), data=fb)
p3=qplot(x=sqrt(friend_count), data=fb)
grid.arrange(p1,p2,p3,ncol=1)

#method 2: add a scaling layer
```{r}
p1 <- ggplot(aes(x=friend_count), data=fb) + geom_histogram()
p2 <- p1+ scale_x_log10()
p3 <- p1 + scale_x_sqrt()
grid.arrange(p1,p2,p3,ncol=1)
```

#3-32

#wrapper
```{r}
logScale = qplot(x=log10(friend_count), data=fb)
countScale = ggplot(aes(x=friend_count), data=fb) + 
  geom_histogram() + scale_x_log10()
grid.arrange(logScale, countScale, ncol=2)
```

#scaling layer
```{r}
qplot(x=friend_count, data=fb) + scale_x_log10()
```

#3-33
#frequency polygon (before we had histograms)
#good for comparing 2 histogram distributions
```{r}
qplot(x=friend_count, data=subset(fb, !is.na(gender)),
      binwidth=10) +
  scale_x_continuous(lim=c(0,1000), breaks=seq(0,1000,50)) +
  facet_wrap(~gender)
```

#geom
```{r}
qplot(x=friend_count, data=subset(fb, !is.na(gender)),
      binwidth=10, geom = 'freqpoly', color=gender)  +
  scale_x_continuous(lim=c(0,1000), breaks=seq(0,1000,50))
```

#change y-axis to show proportions
```{r}
qplot(x=friend_count, y = ..count../sum(..count..), 
      data=subset(fb, !is.na(gender)),
      xlab = 'friend count',
      ylab = 'proportion of users with that friend count',
      binwidth=10, geom = 'freqpoly', color=gender)  +
  scale_x_continuous(lim=c(0,1000), breaks=seq(0,1000,50))
```

#3-34
#which gender creates more likes, create same freq polygon
```{r}
qplot(x=www_likes, 
      #y = ..count../sum(..count..), 
      data=subset(fb, !is.na(gender)),
      xlab = 'www likes receieved',
      #ylab = 'proportion of users with that # of likes recieved',
      #binwidth=1, 
      geom = 'freqpoly', color=gender)  +
  #scale_x_continuous(lim=c(0,50), breaks=seq(0,50,5)) +
  scale_x_log10()
```

#3-35
#numerical summary - who has more likes
#1 - www_like count for males
males = subset(fb, gender='male'); summary(males)
females = subset(fb, gender='female'); summary(females)

#2 - which gender has more likes

by(fb$www_likes, fb$gender, sum)

# by ( column/data, the 1/0 we split by, the fxn we want)

#3-37
#boxplots of friend count by gender
#quickly see difference of distributions
qplot(x=gender, y=friend_count,
      data = subset(fb, !is.na(gender)),
      geom='boxplot'  )

#boxplot outlier when outside of 1.5x median

#3-38
#make it readable
qplot(x=gender, y=friend_count,
      data = subset(fb, !is.na(gender)),
      geom='boxplot',
      ylim=c(0,750))
#we removed 4600 datapoints (ones more than 750)

#same exact plot below
```{r}
qplot(x=gender, y=friend_count,
      data = subset(fb, !is.na(gender)),
      geom='boxplot') +
  scale_y_continuous(limits = c(0,750))
```

#best way - cord cartesian layer, doesnt lose values
#box has moved closer to 250 now since high-outliers kept
```{r}
qplot(x=gender, y=friend_count,
      data = subset(fb, !is.na(gender)),
      geom='boxplot') +
  coord_cartesian(ylim=c(0,250))
```

#3-39
#look at values, comparing them to plot
by(fb$friend_count, fb$gender, summary)

#3-40
#who initiated more friendships
```{r}
qplot(x=gender, y=friendships_initiated,
      data = subset(fb, !is.na(gender)),
      geom='boxplot') +
  coord_cartesian(ylim=c(0,200))
```

by(fb$friendships_initiated, fb$gender, summary)

#3-41
#getting logical
#convert 0 values to binary T/F
#used instead of how many times they used it
summary(fb$mobile_likes)
summary(fb$mobile_likes > 0)

```{r}
fb$mobile_check_in <- ifelse(fb$mobile_likes > 0, 1, 0)
fb$mobile_check_in <- factor(fb$mobile_check_in)
summary(fb$mobile_check_in)
```

#3-42
#what percent of users?
```{r}
sum(fb$mobile_check_in == 1)/length(fb$mobile_check_in)
```

#3-43,44
#types of values, dist, miss/outliers
#histogram, boxplots, frequency polygons
#change the ylim, the binwidth, convert_x_log

#4 - lessons b/w 2 variables
#data aggregation, conditional means, sctrplot
#looked at hist, then x=actual, y=percieved

#4-3
qplot(x=age, y=friend_count, data=fb)
#same as above
qplot(age, friend_count, data=fb)

#4-5
#use aesthetic wrapper, say afterword what type plot
ggplot(aes(x=age, y=friend_count), data=fb) + geom_point() +
  xlim(13,90)

summary(fb$age)

#4-6
#overplotted young,lo-count so we
#points smaller
#jitter so it darkens the lower values
ggplot(aes(x=age, y=friend_count), data=fb) + 
  geom_jitter(alpha=1/20) +
  xlim(13,90)

#4-8
#coord-trans
#add this layer and age axis sqrted
#friend cnt conditional on age
#adding jitter - wed have to say it for only ages
#noise for 0 counts - breaks it
#now no warning and no negatives
ggplot(aes(x=age, y=friend_count), data=fb) + 
  geom_point(alpha=1/20, position=position_jitter(h=0)) +
  xlim(13,90) +
  coord_trans(y='sqrt')

#4-10
#friends initiated and age
ggplot(aes(x=age, y=friendships_initiated), data=fb) +
  geom_point(alpha=1/10, position=position_jitter(h=0)) +
  xlim(13,90) +
  coord_trans(y='sqrt')

#4-12
#transformed axes - as a % of friend count
#conditional means
library(dplyr)
#filter, group.by, mutate, arrange

#group df by age
age_groups <- group_by(fb, age)

#the below gives us new df w/ 1 observation per age
#columns are age, mean, med, n

fb.fc_by_age <- summarise(
  age_groups,
  friend_count_mean = mean(friend_count),
  friend_count_med = median(friend_count),
  n = n())

#this orders the ages from 1-100
fb.fc_by_age <- arrange(fb.fc_by_age, age)

head(fb.fc_by_age)

#other way to do this
fb %.%
  group_by(age) %.%
  summarise(
    age_groups,
    friend_count_mean = mean(friend_count),
    friend_count_med = median(friend_count),
    n = n()) %.%
  arrange(age)

head(fb.fc_by_age,20)

#4-14
#plot avg friend count vs age
ggplot(aes(age,friend_count_mean), data=fb.fc_by_age) +
  geom_line()

#4-15
#2 on top of each other
#histogram and
#conditional mean (friend_count given age)
ggplot(aes(x=age, y=friend_count), data=fb) +
  geom_point(alpha=1/20, 
             position=position_jitter(h=0),
             color='orange') +
  xlim(13,90) +
  coord_trans(y='sqrt') +
  geom_line(stat='summary', fun.y=mean)

# add 25/75 quantiles on the plot
ggplot(aes(x=age, y=friend_count), data=fb) +
  geom_point(alpha=1/20, 
             position=position_jitter(h=0),
             color='orange') +
  xlim(13,90) +
  coord_trans(y='sqrt') +
  geom_line(stat='summary', fun.y=mean) +
  geom_line(stat='summary', fun.y=quantile, probs = .25,
            linetype=2, color='blue') +
  geom_line(stat='summary', fun.y=quantile, probs = .5,
            color='blue') +
  geom_line(stat='summary', fun.y=quantile, probs = .75,
            linetype=2, color='blue')

#same but with coord-cartesian layer (not throwing some out)
ggplot(aes(x=age, y=friend_count), data=fb) +
  coord_cartesian(xlim=c(13,90), ylim=c(0,1000)) +
  geom_point(alpha=1/20, 
             position=position_jitter(h=0),
             color='orange') +
  geom_line(stat='summary', fun.y=mean) +
  geom_line(stat='summary', fun.y=quantile, probs = .1,
            linetype=2, color='blue') +
  geom_line(stat='summary', fun.y=quantile, probs = .5,
            color='blue') +
  geom_line(stat='summary', fun.y=quantile, probs = .9,
            linetype=2, color='blue')

#4-17
#pair raw data with summary data

#4-18,4-19
#stat95 course also
#summarize strength of relationship with correlation

#core.test -> find r using 2 variables
#takes 2 vectors, calculates r
?cor.test

cor.test(fb$age, fb$friend_count, method = 'pearson')

#4-21
with(subset(fb, age<=70), cor.test(age, friend_count))
#as age up, very slight friends down

#4-22
#spearman
with(subset(fb, age<=70),
     cor.test(age, friend_count, method = 'spearman'))

#4-23
#scatterplot correlated variables
# www_likes_recieved compared to likes_Recieved
ggplot(aes(x = www_likes_received, y=likes_received), data=fb) +
  geom_point()

#same but 0,.95 quantile
ggplot(aes(x = www_likes_received, y=likes_received), data=fb) +
  geom_point() +
  xlim(0, quantile(fb$www_likes_received, .95)) +
  ylim(0, quantile(fb$likes_received, .95)) +
  geom_smooth(method='lm', color = 'red')

#4-26
#whats corr b/w 2, include top 3, round to 3
cor.test(fb$www_likes_received, fb$likes_received)

#measure correlation b/w variables first, can throw some out

#4-28
install.packages('alr3')
library(alr3)
data(Mitchell)

#create scatterplot of temperature vs months
ggplot(data=Mitchell, aes(x=Month, y=Temp)) +
  geom_point()

#or
qplot(data=Mitchell, Month, Temp)

#4-31
#whats correlation bw 2
cor.test(Mitchell$Month, Mitchell$Temp)

#4-32
#months 1-22 dont make sense
#add detail so its jan-dec
ggplot(data=Mitchell, aes(x=Month, y=Temp)) +
  geom_point() +
  scale_x_discrete(breaks = seq(0, 203, 12))

#4-35
#stretch it out
#50% wider than it is tall

#4-36
ggplot(aes(x=age, y=friend_count_mean), data = fb.fc_by_age) +
  geom_line()

head(fb.fc_by_age, 10)
fb.fc_by_age[17:19,]

#4-36
#create an age_and_months variable
fb$age_with_months <- fb$age + (12- fb$dob_month)/12

#4-38
#use dplyr to get new df df.fc_with_age_months

age_months_groups = group_by(fb, age_with_months)

#video
#fb.fc_by_age_months = summarise(age_with_months)

fb.fc_by_age_months = summarise(
  age_months_groups,
  friend_count_mean = mean(friend_count),
  friend_count_med = median(friend_count),
  n = n())

fb.fc_by_age_months = arrange(df.fc_by_age_months, age_with_months)

head(fb.fc_by_age_months)

#could also do
library(dplyr)
fb.fc_by_age_months = fb %.%
  group_by(age_with_months) %.%
  summarise(friend_count_mean = mean(friend_count),
            friend_count_median = median(friend_count),
            n=n()) %.%
  arrange(age_with_months)

head(fb.fc_by_age_months)

#4-40
#plot mean friend count vs age_in_months
#subset data frame - only users < 71

ggplot(aes(x=age_with_months, y=friend_count_mean),
       data = subset(fb.fc_by_age_months, age_with_months < 71)) +
  geom_line()

#4-42
#plot age_months and age
m1 = ggplot(aes(x=age, y=friend_count_mean),
            data = subset(fb.fc_by_age, age < 71)) +
  geom_line() + geom_smooth()

m2 = ggplot(aes(x=age_with_months, y=friend_count_mean),
            data = subset(fb.fc_by_age_months, age_with_months < 71)) +
  geom_line() + geom_smooth()

#age / 5, rounded * 5, stats summary, mean_friend_count
#fewer data points, large binwidth
m3 = ggplot(aes(x=round(age/5)*5, y=friend_count),
            data = subset(fb, age < 71)) +
  geom_line(stat='summary', fun.y=mean)

library(gridExtra)
grid.arrange(m2,m1,m3, ncol=1)

#these models based on idea that its smooth, its not
#scatterplots, conditional means
#jitter, transparency to reduce overplotting

#5-3
#3+ variables

#add the mean to each genders boxplot
ggplot(aes(x=gender, y=age),
       data = subset(fb, !is.na(gender))) + geom_boxplot() +
  stat_summary(fun.y=mean, geom='point', shape = 4)

#line plots of friend count by age. 2 lines for 2 genders
ggplot(aes(x=age, y=friend_count),
       data = subset(fb, !is.na(gender))) + 
  geom_line(aes(color=gender), stat = 'summary', fun.y = median)

#create the df w/ the mn/med friend-count and # for each age-gender
#chain funxtions %
library(dplyr)
fb.fc_by_age_gender = fb %>%
  filter(!is.na(gender)) %>%
  group_by(age, gender) %>%
  summarise(mean_friend_count = mean(friend_count),
            median_friend_count = median(friend_count),
            n = n()) %>%
  ungroup() %>%
  arrange(age)

head(fb.fc_by_age_gender)

#5-5
#construct the plot that shows median friend count for gender by age
ggplot(aes(x=age, y=median_friend_count),
       data = fb.fc_by_age_gender) + 
  geom_line(aes(color=gender))

#5-7, 5-8
#data is in long format m f is repeated
# make it so 1 row for each age

#5-9
# long -> wide
library(reshape2)

fb.fc_by_age_gender.wide = dcast(fb.fc_by_age_gender,
                                 age ~ gender,
                                 value.var = 'median_friend_count')

head(fb.fc_by_age_gender.wide)

#melt fxn brings wide -> long

#5-10, 5-11
#reshape the above plot so it shows females 1.5x fc as males
ggplot(aes(x=age, y=female/male),
       data = fb.fc_by_age_gender.wide) +
  geom_line() +
  geom_hline(yintercept = 1, alpha = .3, linetype=2)

#maybe new fb countries are all men and have low friend counts

#5-12
#fb tenure, # of days -> friends

#5-13
#create variable year joined
fb$year_joined <- floor(2014 - fb$tenure/365)

#5-14
#look at summary and table of it to see distribution
summary(fb$year_joined)
table(fb$year_joined)

#5-15
#cut the variable 04-09, 09-11, 11-12, 12-14
fb$year_joined_bucket <- cut(fb$year_joined,
                             c(2004, 2009, 2011, 2012, 2014))

#5-16
table(fb$year_joined_bucket, useNA = 'ifany')

#plot x=age, y = fc, each year-join bucket has line on graph
ggplot(aes(x=age, y=friend_count),
       data = subset(fb, !is.na(year_joined_bucket))) +
  geom_line(aes(color = year_joined_bucket), 
            stat='summary', fun.y = median)

#5-18
#plot the same but mean and grand mean
ggplot(aes(x=age, y=friend_count),
       data = subset(fb, !is.na(year_joined_bucket))) +
  geom_line(aes(color = year_joined_bucket), 
            stat='summary', fun.y = mean) +
  geom_line(stat='summary', fun.y = mean, linetype=2)

#much of the data is from recently joined ppl

#5-20
#how many friends user has per day
#median rate, max rate
#fb$friend_per_day = fb$friend_count / fb$tenure
#summary(subset(fb$friend_per_day, fb$friend_count > 0))

with(subset(fb, tenure >= 1), summary(friend_count/tenure))

#5-22
#create line graph of y= friendships-initiated per day , x= tenure
ggplot(aes(x=tenure, y=friendships_initiated/tenure),
       data = subset(fb, tenure > 0)) +
  geom_line(aes(color = year_joined_bucket), 
            stat='summary', fun.y = median)

#5-24
#that graph is noisy/fat. make it smoother
ggplot(aes(x=tenure, y=friendships_initiated/tenure),
       data = subset(fb, tenure > 0)) +
  geom_smooth(aes(color = year_joined_bucket))

#5-26
#nfl fans: ratios of +/- words over 4 months
#aggregated averages up to 1 day
#predict y=sentiment from x=time
#colored lines for wins and loses
#discrete jumps within games -> use a 7-day moving average
#combine with spines (added dummy variables with post-game periods)

#5-28
#new dataset - household purchases of 5 yogurts - 1 row per buy
yo = read.csv('yogurt.csv')
str(yo)
summary(yo)

# convert the id variable int to a factor
yo$id = factor(yo$id)

# create histogram of the yogurt prices
qplot(data=yo, x=price)

#now nicer, with orange color
qplot(data=yo, x=price, fill = I('#F79420'))

#if we chose a large binwidth, it is biased. we miss price jumps
#this data is very discrete, plot should be too
qplot(data=yo, x=price, fill = I('#F79420'), binwidth=10)

#if u just look at 5-number summary, you could miss discrete prices
# a clue is that 75percentile is same as maximum
length(unique(yo$price))
table(yo$price)

#on 1 purchase-occasion, how many 8oz yogurts do they purchase
#transform fxn

#create new variable all_purcases
yo = transform(yo, all.purchases = strawberry + blueberry +
                 pina.colada + plain + mixed.berry)

#5-32
#create a hist of new variable
qplot(x=all.purchases, data=yo)

#error says binwidth defaulted to range/30, which is 2/3
range(yo$all.purchases)
qplot(x=all.purchases, data=yo, binwidth=1, fill = I('#099DD9'))

#most ppl buy 1 or 2 at once, not 3-21

#5-33
#scatterplot of x=time, y=price
#overplot also

#what i wouldve done - hard with such discrete prices
qplot(x=time, y=price, data = yo)

#need to make the multiple dots in 1 spot stand out - add a jitter
# setting alpha = 1/4 means it needs 4 points to stand out
ggplot(aes(x=time, y=price), data = yo) +
  geom_jitter(alpha = 1/5)

# the modal or most common prices increase over time

#5-35
# often useful to look at a small sample of the data
# comes before using within-home variance as a model

#make reproducible, then pick 16 by sampling the levels (of factor var)
set.seed(4230)
sample.ids <- sample(levels(yo$id), 16)

#i wouldve plotted the same as earlier
# can subset data1, specific yo$id in sample-in-data1
qplot(x=time, y=price,
      data = subset(yo, id %in% sample.ids))

#plot each purchase occasion - time, price, size
#the facet-wrap creates 16 different plots
# each shows these 16 sessions, x=time, y=price, each pt is a buy
#  need to add at least 1 of line and point
#   add both for visibility

ggplot(aes(x=time, y=price),
       data = subset(yo, id %in% sample.ids)) +
  facet_wrap(~id) +
  geom_line() +
  geom_point()

#same but consider the number of items in the size of the dot
ggplot(aes(x=time, y=price),
       data = subset(yo, id %in% sample.ids)) +
  facet_wrap(~id) +
  geom_line() +
  geom_point(aes(size=all.purchases), pch=1)

#create similar plot for different set of 16 houses

#5-36
# with observations over time, can look at multiple users w/ facet
#fb isnt great at friending over time, its a cross-section
# if fb like yogurt data, could look at friends over time

#5-38
#scatterplot matrix
# scatterplots not suited for categorical
# boxplots or histograms
install.packages("GGally")
library(GGally)

theme_set(theme_minimal(20))

#going to subset from fb, sample from it
set.seed(1836)
fb_subset = fb[, c(2:15)]
names(fb_subset)

#takes an hour to run!
#ggpairs(fb_subset[sample.int(nrow(fb_subset), 1000), ])

#5-40
#even more variables - gene expression - 6830 genes and reference
nci = read.table('nci.tsv')

#5-41
#heat map
#difference in over/under expression vs benchmark

#6-1
#scraped and formatted a diamond price set
data(diamonds)

#scatterplot
#try 1
qplot(data=diamonds, x=carat, y=price)

#want axes to only go up to almost top. skew makes it unreadable
qplot(data=diamonds, x=carat, y=price,
      xlim = c(0, quantile(diamonds$carat, .99)),
      ylim = c(0, quantile(diamonds$price, .99)))

#same but adding fill, color, shape
qplot(data=diamonds, x=carat, y=price,
      xlim = c(0, quantile(diamonds$carat, .99)),
      ylim = c(0, quantile(diamonds$price, .99))) +
  geom_point(fill=I('#F79420'), color=I('black'), shape=21)

#add a linear trend line, not perfect tho
qplot(data=diamonds, x=carat, y=price,
      xlim = c(0, quantile(diamonds$carat, .99)),
      ylim = c(0, quantile(diamonds$price, .99))) +
  geom_point(fill=I('#F79420')) +
  stat_smooth(method = 'lm')

#6-9
library(scales)
library(memisc)
library(MASS)
library(car)
library(lattice)

##ggpairs plots each variable against each other

##going to sample so less slow
# set.seed(20022012)
# diamond_samp = diamonds[sample(1:length(diamonds$price), 10), ]
# ggpairs(diamond_samp,
#         wrap = c(shape = I('.'), outlier.shape = I('.')))

#qual-qual is grouped histograms
#quant-quant is scatterplot

#qual-quant is boxplots
#quant-quant is r

#6-12
plot1 = qplot(data=diamonds, x=price, binwidth=100) +
  ggtitle('Price')

plot2 = qplot(data=diamonds, x=price, binwidth=.01) +
  ggtitle('Price (log10)') +
  scale_x_log10()

#2 histograms of price, on 2 different scales
library(gridExtra)
library(grid)
grid.arrange(plot1,plot2, ncol=2)

#bimodal log10 scale - 2 class rich/poor buyer

#6-15

#replot, x=carat, y=price on log10 scale
qplot(carat, price, data=diamonds) +
  scale_x_continuous(trans= log10_trans()) +
  ggtitle('Price (log10) by Carat')

# fxn to transform the carat variable
# takes cuberoot of input
# can also undo it with inverse
cuberoot_trans = function() trans_new('cuberoot',
                                      transform = function(x) x^(1/3),
                                      inverse = function(x) x^3)

# use fxn
ggplot(aes(carat, price), data=diamonds) +
  geom_point() +
  scale_x_continuous(trans = cuberoot_trans(),
                     limits = c(.2, 3),
                     breaks = c(.2, .5, 1, 2, 3)) +
  scale_y_continuous(trans = log10_trans(),
                     limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Carat')

#it looks linear can use linear-tools on it

#6-16
#table on carat and price, then sort, look at top 6
head(sort(table(diamonds$carat), decreasing=T))
head(sort(table(diamonds$price), decreasing=T))

#lots of data, so overplotting -> obscures density and sparcity at pts

#6-17
#make points smaller with jitter, and by adding transparency
ggplot(aes(carat, price), data=diamonds) +
  geom_point(alpha = .5, size = .75, position='jitter') +
  scale_x_continuous(trans = cuberoot_trans(),
                     limits = c(.2, 3),
                     breaks = c(.2, .5, 1, 2, 3)) +
  scale_y_continuous(trans = log10_trans(),
                     limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat')

#clarity, cut, color as factors
library(RColorBrewer)
ggplot(aes(x=carat, y=price, color=clarity), data=diamonds) +
  geom_point(alpha = .5, size = 1, position='jitter') +
  scale_color_brewer(type = 'div',
                     guide=guide_legend(title='Clarity',
                                        reverse=TRUE,
                                        override.aes=list(alpha=1, size=2))) +
  scale_x_continuous(trans = cuberoot_trans(),
                     limits = c(.2, 3),
                     breaks = c(.2, .5, 1, 2, 3)) +
  scale_y_continuous(trans = log10_trans(),
                     limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) vs \nCube-Root of Carat and Clarity')

#6-22
#now color pts by cut, not clarity
ggplot(aes(x=carat, y=price, color=cut), data=diamonds) +
  geom_point(alpha = .5, size = 1, position='jitter') +
  scale_color_brewer(type = 'div',
                     guide=guide_legend(title='Clarity',
                                        reverse=TRUE,
                                        override.aes=list(alpha=1, size=2))) +
  scale_x_continuous(trans = cuberoot_trans(),
                     limits = c(.2, 3),
                     breaks = c(.2, .5, 1, 2, 3)) +
  scale_y_continuous(trans = log10_trans(),
                     limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) vs \nCube-Root of Carat and Cut')

#most are ideal, very few different

#6-28
ggplot(aes(x=carat, y=price, color=color), data=diamonds) +
  geom_point(alpha = .5, size = 1, position='jitter') +
  scale_color_brewer(type = 'div',
                     guide=guide_legend(title='Color',
                                        reverse=FALSE,
                                        override.aes=list(alpha=1, size=2))) +
  scale_x_continuous(trans = cuberoot_trans(),
                     limits = c(.2, 3),
                     breaks = c(.2, .5, 1, 2, 3)) +
  scale_y_continuous(trans = log10_trans(),
                     limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) vs \nCube-Root of Carat and Color')

#made it so best color is at top, reverse=False

#6-31
#can create models using the lm fxn
#lm(y~x)
#lm(log(price) ~ carat^(1/3))

#flawless diamond becomes exponentially rarer as carat increases

#6-33
#I wrapper around each - as is - tells r to use expression in i fxn
#transforms variable before using it in regression
#instead of telling R to interpret symbols as part of regression

#add simple updates by adding more variables

m1 = lm(I(log(price)) ~ I(carat^(1/3)), data=diamonds)
m2 = update(m1, ~ . + carat)
m3 = update(m1, ~ . + cut)
m4 = update(m1, ~ . + color)
m5 = update(m1, ~ . + clarity)
mtable(m1,m2,m3,m4,m5)

#6-34
#our model is
#ln(price) = .415 + 9.144*carat^(1/3) - 1.093*carat + 
#(series of coefficients * each factor) * cut + 
#c2*color * c3*clarity + error

#data from 08-> 14, inflation
# got predictions way too low, prices plummeted in 08, grew a lot
# china demand up
# prices grew unevenly

#6-36
#python script w up to date values - 500k cases
library('RCurl')
install.packages('bitops')
library('bitops')

diamondsurl = getBinaryURL('https://raw.github.com/solomonm/diamonds-data\
/master/BigDiamonds.Rda')
load(rawConnection(diamondsurl))

#6-37
#with new data
diamondsbig$logprice = log(diamondsbig$price)
m1 = lm(logprice ~ I(carat^(1/3)),
        data=diamondsbig
        [diamondsbig$price < 10000 & diamondsbig$cert=="GIA",])
m2 = update(m1, ~ . + carat)
m3 = update(m1, ~ . + cut)
m4 = update(m1, ~ . + color)
m5 = update(m1, ~ . + clarity)
mtable(m1,m2,m3,m4,m5)

#6-38
#make predictions!
#ex - rnd1, vg, i, vs1, 5601
thisDiamond = data.frame(carat=1.00, cut="V.Good",
                         color="I", clarity="VS1")
modelEstimate = predict(m5, newdata=thisDiamond,
                        interval="prediction", level=.95)
exp(modelEstimate)
#it was too low, and the range is 3000! too large!
#linear model multiplies
