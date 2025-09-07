import numpy as np
a = np.array([1,2,3])
b = 2
print(a + b)   # [3,4,5]

m = np.ones((3,3),dtype=int)
n = np.array([1,2,3])
print(m + n)   # broadcast row

