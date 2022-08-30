import numpy as np

m,n = input().split()
m = int(m)
n = int(n)
a = np.empty([m], dtype=object)
for i in range(0,m)
    a[i] = input().split(' ')

a = np.vstack([i for i in a])

a = np.transpose(a)
print('n'.join('t'.join(map(str, row)) for row in a))