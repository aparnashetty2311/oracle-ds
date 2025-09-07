import numpy as np
a = np.arange(16)
print(a)
b=a.reshape(4,4)
print(b)
'''print("=================")
print(a.reshape(3,4))     # reshape

print("=================")
print(a.reshape(-1,6))    # infer rows
print("=================")
print(a.flatten())        # flatten
print("=================")
print(a.ravel())          # fast flatten
print("=================")
'''
print(b.T)                # transpose
print("=================")

#print(np.resize(a,(2,8))) # resize with repeat
