from scipy.stats import bernoulli
import numpy as np

def bernoulli_trial(p, n):
    """create Bernoulli sample of size n, with heads given by p
       return the number of heads"""
    rv = bernoulli.rvs(p,size=n)
    return np.sum(rv)

samples = [10,100,1000,10000,100000,1000000,10000000]
p=0.3
print('Probability of head : {0:.3f}'.format(p))
print('Sample size       Heads')
for n in samples:
    heads = bernoulli_trial(p,n)
    print('{0:11.0f}   {1:9.0f}'.format(n,heads))