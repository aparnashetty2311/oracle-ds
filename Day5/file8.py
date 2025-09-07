import numpy as np
A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])

print(A @ B)               # matrix multiplication

print(np.dot(A,B))
print(np.matmul(A,B))
print(np.linalg.det(A))    # determinant
print(np.linalg.inv(A))    # inverse
print(np.linalg.eig(A))    # eigenvalues
print(np.trace(A))         # trace
print(A.T)                 # transpose
