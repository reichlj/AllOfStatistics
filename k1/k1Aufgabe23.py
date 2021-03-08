from scipy.stats import randint
A = {2,3,6}
B = {1,2,3,4}
C = A.intersection(B)

n = 10000000
uniform_dist = randint(low=1,high=7)
samples = uniform_dist.rvs(size=n)
countA = 0
countB = 0
countC = 0
for k in range(n):
    if samples[k] in A:
        countA +=1
    if samples[k] in B:
        countB +=1
    if samples[k] in C:
        countC +=1
print('Sample size: ',n)
print('P(A)=1/2  found: {0:.4f}'.format(countA/n))
print('P(B)=2/3  found: {0:.4f}'.format(countB/n))
print('P(C)=1/3  found: {0:.4f}'.format(countC/n))
print('P(A)*P(B) found: {0:.4f}'.format(countA/n*countB/n))
