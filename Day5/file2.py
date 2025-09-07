import numpy as np
'''
a=np.arange(15,25)
print(a)

print(a[0])
print(a[-1])

# 0   1  2  3  4  5  6  7  8  9
# 15 16 17 18 19 20 21 22 23 24
# -10 -9 -8 -7 ... -1

print(a[2:7])    # 2 3 4
print(a[:5])
print(a[::4])   #[start : stop : step]
print(a[3:])

matrix = np.array(
    [
    [1,2,3],
    [4,5,6]
    ])
print(matrix[1,2])  # element at row1,col2
print(matrix[:,0])
print(matrix[:,1])  # 2nd column
print(matrix[:,2])
print(matrix[0,:])  # 1st row
print(matrix[1,:])

'''

np6=np.array([
    [3,5,7,8,2,3],
    [2,7,3,2,3,6]])
print(np6[1,2]) #3

print(np6[0,4]) #2

print(np6[0:2])

print(np6[0:2 , 3:6])   #  0:2   Row values 3:6   column values 
