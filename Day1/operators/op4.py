x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(id(x))
print(id(y))
print(id(z))

print(x is z)	# Output: True 
print(x is y)	# Output: False 
print(x is not y)
