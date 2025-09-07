import numpy as np
array1= np.array([23,34,45,12])

print(array1, "  ", id(array1))
print(array1.ndim)
print("share ", array1.shape)
for i in range(4):
    print(i , "=> " , array1[i], " id is ", id(array1[i]))

A = np.array( [ [10,20,30], [40,50,60],[40,50,60]] )
print(A) 

print(A.ndim) 
print(A.shape)
