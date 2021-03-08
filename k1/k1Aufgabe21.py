from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt
from timeit import Timer

def get_data_loop():
    count = 0
    for k in range(samples.size):
        data[k, 0] = k + 1
        if samples[k] == 1:
            count = count + 1
        data[k, 1] = count
        data[k, 2] = count / data[k, 0]

def get_data_vectorized():
    data[:, 0] = np.arange(1, samples.size + 1)
    data[:, 1] = np.cumsum(samples)
    data[:, 2] = data[:, 1] / data[:, 0]


n = 10000
p = 0.3
# sample of size n from Bernoulli process with heads given by p
samples = bernoulli.rvs(p, size=n)

# calculate heads and p as a function of the number of trials
data = np.zeros((n,3))
timer_obj = Timer("get_data_loop()","from __main__ import get_data_loop")
print('For-Loop {0:.6f}'.format(timer_obj.timeit(10)))

# vectorized version
# calculate heads and p as a function of the number of trials
data = np.zeros((n,3))
timer_obj = Timer("get_data_vectorized()","from __main__ import get_data_vectorized")
print('Vectorized {0:.6f}'.format(timer_obj.timeit(10)))
get_data_vectorized()


plt.plot(data[:,0],data[:,2],color='blue')
plt.hlines(p,1,n,color='red',linestyle='--')
plt.title("N={0}  Heads={1:.0f}  p={2:6.4f}".format(n,data[-1,1],p))
plt.xlabel('Number of Trials')
plt.ylabel('Proportion of Heads')
plt.show()
print(data)