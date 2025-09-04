my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

for i in range(3):
    print(i , " => " , my_tuple[i])

print(type(my_tuple))
print(id(my_tuple))
print(my_tuple.index("mouse"))

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3),100,200)

print(type(my_tuple))
print(id(my_tuple))

t=list(my_tuple)
print(t)