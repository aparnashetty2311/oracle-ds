def sum(x,y):
    return x+y


print(sum(10,20))

add=lambda x,y : x+y
print(add(10,20))

msg=lambda name: print ("Hello",name)
msg("Nageswara")

msg=lambda : print ("Hello")
msg()

msg=lambda : 1000
print(msg)
