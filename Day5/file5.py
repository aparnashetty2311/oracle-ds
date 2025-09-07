import numpy as np



arr = np.arange(20,30)   # [0 1 2 3 4 5 6 7 8 9]
#print(np.split(arr, 2))

print(np.split(arr,[3,8]))


A = np.array([[1, 2],
              [3, 4]])

print(A)

inv_A = np.linalg.inv(A)
print("Inverse:\n", inv_A)

A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

inv_A = np.linalg.inv(A)
print("Inverse:\n", inv_A)

