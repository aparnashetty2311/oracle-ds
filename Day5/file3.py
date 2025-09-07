import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])

print(x + y)      # add
print(np.add(x,y))

print(x - y)      # subtract
print(x * y)      # elementwise multiply
print(x / y)      # elementwise divide
print(x % y)      # modulus
print(x ** 2)     # power

print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))
