'''
Probability: chance of something favorable occurring:
eg. getting odd number when you roll a dice:  3/6 = 1/2 = 0.5

Probability distribution:
1. Discrete distribution:
    PMF - Probability Mass Function
    a. What is the probability of getting exect 10 times 5 when I roll a dice 100 times
    CDF - Cumulative Distribution Function
    a. What is the probability of getting 10 or less times 5 when I roll a dice 100 times
    PPF - Percent Point function
    RVS - generates values for the distribution

    Bernouli's distribution - discrete distribution with one event
    p = success probability
    q = failure probability, q = 1-p
    e.g. What's the probability of getting 5 when I roll a dice once
    p = prob of getting 5 = 1/6
    q = prob of not getting 5 = 1 - 1/6  = 5/6

    Binomial distribution: Given n of trials, what is the probability of
    getting k number of favorable trials.

2. Continuous distribution:

We will use Scipy here. You need to install scipy - pip install scipy
'''
from scipy.stats import bernoulli
import seaborn as sns
import matplotlib.pyplot as plt

data = bernoulli.rvs(size=2000, p=1 / 2)
ax = sns.displot(data, kde=True)
plt.show()

# calculating PMF
pmf_val = bernoulli.pmf(1, p=1 / 6)
print("PMF for winning in game of dice (getting 5) is", pmf_val)
pmf_val = bernoulli.pmf(0, p=1 / 6)
print("PMF for losing in game of dice (not getting 5) is", pmf_val)

## BINOMIAL DISTRIBUTION
'''
An agent sells life insurance policies to five equally aged, healthy people. 
According to recent data, the probability of a person living in 
these conditions for 30 years or more is 2/3. 
Calculate the probability that after 30 years:

1. All five people are still living.
2. At least three people are still living.
3. Exactly two people are still living.
'''
from scipy.stats import binom

n = 5  # total no. of ppl living beyond 30 yrs
p = 2 / 3  # prob of person living
# for sol_3, exact 2 ppl, that means
k_sol3 = 2
# this is a pmf problem
sol_3 = binom.pmf(n=n, p=p, k=k_sol3)
print("Probability of Exactly two people are still living = ", sol_3)

print("Probability of 0,1,2,3,4 or 5 ppl alive = ", binom.pmf(n=n, p=p, k=0) +
      binom.pmf(n=n, p=p, k=1) + binom.pmf(n=n, p=p, k=2) + binom.pmf(n=n, p=p, k=3) +
      binom.pmf(n=n, p=p, k=4) + binom.pmf(n=n, p=p, k=5))

## At least three people are still living
print("Probability of At least three people are still living = ", binom.pmf(n=n, p=p, k=3) +
      binom.pmf(n=n, p=p, k=4) + binom.pmf(n=n, p=p, k=5))
## (3,4,5) = 1 - (0,1,2)
print("Probability of At least three people are still living = ", 1 - binom.cdf(n=n, p=p, k=2))

#  All five people are still living.
print("Probability of All five people are still living = ", binom.pmf(n=n, p=p, k=5))

'''
Probability Distribution:

An average of 0.61 soldiers died by horse kicks per year in each
Prussian army corps. You want to calculate the probability
that exactly two soldiers died in the VII Army Corps in 1898,
assuming that the number of horse kick deaths per year follows a
Poisson distribution.
'''
from scipy.stats import poisson

avg = 0.61
poi_rate = poisson(avg)
prob = poi_rate.pmf(2)
print("Probability that exactly two soldiers died =", prob)
prob = poi_rate.cdf(2)
print("Probability that at max two soldiers died =", prob)

'''
Continous distribution
Normal Distribution:

In a certain exam, average marks scored by people appearing is 490
with standard deviation of 20
In what % of ppl I am ahead of, if I score 525
Z score of 525 = (525 - 490) / 20 = 35/20 = 1.75
    from table: -inf to 0 = 0.5
                -inf to -1.75 = 0.0401
                -1.75 to 0 = 0.5 - 0.0401 = 0.4599
                -inf to 1.75 = 0.5 + 0.4599 = 0.9599 = 95.99%
Number of people above me: 1- 95.99%

.... if my score is 510 : (at 1 sigma) = 84%
.... if my score is 530 : (at 2 sigma) = 84%
                0 to 2: 95/2 = 47.5 + 50 = 97.5%
'''

from scipy.stats import norm

avg = 490
sd = 20
num = 525
# should we find pdf() or cdf() - we need cdf here
z = (num - avg) / sd
prob = norm.cdf(z)
print("Probability = ", prob)

'''
Population and Sample:
1. You cant access entire population, you decide to work with sample data
2. Once you have your analysis then you need to figure out mechanism to test!
3. test to see if one should believe your data or not

Sampling methods:
 1. Non-stastical method : convenience method, judgemental, snowball, quota sampling
 2. Probabilistic methods : simple random, cluster sampling (create clusters and pick your cluster),
                          systematic sampling, stratified sampling

Hypothesis test:
1. Null Hypothesis (H0) - no impact
2. Alternate Hypothesis (H1) - yes there is impact (+ve or -ve)
3. Result will tell you should you accept or reject Null Hypotheis (based on p value)
    If reject then look at the result and convey if +ve or -ve
'''

'''
ESTIMATION FOR SINGLE POPULATION
1.  Numerical data

We need to use either Z-test or t-test
1.  If Population standard deviation is given and the sample size is >30 : use Z-score to test
2.  Either the population sample is less than 30 or Standard Deviation of population is not available – t-test to test.

Principal says that his 30 students have above average intelligence.
1. GIVEN:
Based on the data:
    1. Mean IQ of the population = 100
    2. Standard deviation is = 15
    3. Mean of the sample (the school in the discussion) = 112
2. PROCESS
H0 => Mean of sample = mean of population
    112 is almost same as 100 =>
    these students of the school has same intelligence level as global mean

H1 => mean of sample > mean of population

3. ALPHA Level (Confidence level) - 95%
Z Score of 1.645 [@ alpha level 0.95 - for one tailed test]

4. Z Score of the data:
Z test =  (sample mean - pop mean)/ (sd / root of n)
where n is number of samples
(112 - 100)/(15 / root of 30)
12 / (15/5.477)
Z = 4.38

Since Z score is greater than alpha value, we reject Null Hypothesis

Population mean of 100 glucose level with sd of 15
Sample of 30 - and after a certain diet their glucose level went uptp 140

Prove that specific diet has an impact on the glucose level

This problem is different to previous problem because here,
 we are interested in performing 2 Tailed test and in the above school
 example, we were focused on one tailed (higher value)

 Since its a 2-tailed test, we are dividing the alpha value by 2
 = 0.05 / 2 = 0.025 
 Z value here is 1.96

 Z -test: 14.6 - this is greater than z value so we reject the Null Hypothesis

Population mean = 2.5
Sample mean = 3.2
SD of pop = 1.1
 n = 18
Since n <30, we will use t-score to test
Test: Is the mean (3.2) abnormally high?
t-score = (Pop mean - sample mean)/ Standard Error
SE = SD/root n = 1.1/root 18 =0.259
t-score= -2.7
The t-score at DF 17 is less than 0.01 which indicates, we reject Null Hypothesis
So the statement made is True

'''

from scipy.stats import t, norm

alpha = 0.95
z_val = norm.ppf((1 - alpha) / 2)
print("Z Alpha value = ", z_val)

t_val = t.ppf((1 - alpha) / 2, df=17)
print("T Alpha value = ", t_val)

'''
Problem statement: If a woman eats more calories with women compared to when with men
Here we have 2 population - Woman with Women and Woman with Men
we have 2 sample mean - mu1 and mu2

H0 => mu1 = mu2
H1 => mu1 > mu2

Research was conducted, data collected were:
1. In a sample of 45 women, dining with other women, mean was 850 calories, sd = 252
2. In a sample of 25 women, dining with men, mean was 719 calories, sd = 322

Since we dont have population SD, we need to use T-test

'''

sd1, sd2 = 252, 322
mu1, mu2 = 850, 719
n1, n2 = 45, 25
denom = ((sd1 * sd1 / n1) + (sd2 * sd2 / n2)) ** 0.5
num = mu1 - mu2
t_test = num / denom
print("t-score for 2 population = ", t_test)

from scipy.stats import t

df = 45 - 2  # max n -2
p_val = 1 - t.cdf(t_test, df=df)
# for alpha of x, p-value should be less than 1-x to reject Null hypothesis
print("P value =", p_val)
if p_val < 0.05:
    print("We reject the Null hypothesis and claim that Women eat less calories when with men")
else:
    print("We accept Null hypothesis and state that there is no difference in their calories")

print("*****************************")

file = "https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/onewayAnova_data.csv"
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(file)
print(df)
df.boxplot(column=['A', 'B', 'C', 'D'], grid=False)
plt.show()

import scipy.stats as st

fval, pval = st.f_oneway(df['A'], df['B'], df['C'], df['D'])
print(fval, pval)
# higher value for f-stats (fval) is better - method that we chose
# is better by a higher margin (variance)


from scipy.stats import chi2_contingency

data = [[224, 266, 240], [217, 258, 233]]
stat, p, dof, expected = chi2_contingency(data)
print("Stat = ", stat)
print("P-Value = ", p)
print("Degree of freedom = ", dof)
print("Expected value:\n", expected)

# since p>0.05, we accept Null Hypothesis-> there is no connection between
# Gender and the Pets they like

