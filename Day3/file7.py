list1=[1,4,2,3,3,3,2,2,2,3,4,"Nageswara",34.934,34.34,True]
print(list1)

for i in range(15):
    print(i ,"-> " ,list1[i])

print(type(list1))
print(id(list1))
list1.append(1000)
print("---------------------------")
print(list1)
print(id(list1))

list1.insert(2,"Ajay")
print("---------------------------")
print(list1)
print(id(list1))

print(list1.count(4))

list1.insert(20,"Ajay100")
print("---------------------------")
print(list1)
print(id(list1))
list1.insert(10,"Ajay200")
print(list1.index("Ajay200"))  

print("---------------------------")
list1.remove("Nageswara")
print(list1)
print(id(list1))

print("---------------------------")
list1.pop(0)
print(list1)
print(id(list1))

set1=set(list1)

print(set1)

