import numpy as np
A = np.array( [ [10,20,30,40], [50,60,70,80] ] )
print(A.ndim , A.size, A.shape, A.dtype)
B = A.reshape(2,2,2)
print(A)
print("====================")
print(B)
