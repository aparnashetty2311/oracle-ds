import numpy as np



arr = np.arange(12).reshape(4, 3)
print(arr)
parts = np.split(arr, 3, axis=1)
for p in parts:
    print(p,"\n")