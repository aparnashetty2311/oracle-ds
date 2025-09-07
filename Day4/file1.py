emp=[{ "empno":100,
     "empname":"Nageswara",
     "salary":1000.00, 
     "color":{"red","blue","yello"},
     "marks":[23,23,34,12],
     "loc":("india","usa","canada",34,33)
     },
{ "empno":101,
     "empname":"Nageswara",
     "salary":1000.00, 
     "color":{"red","blue","yello"},
     "marks":[23,23,34,12],
     "loc":("india","usa","canada",34,33)
     },
     { "empno":102,
     "empname":"Nageswara",
     "salary":1000.00, 
     "color":{"red","blue","yello"},
     "marks":[23,23,34,12],
     "loc":("india","usa","canada",34,33)
     }]


print(emp)
'''
print(emp.get("empno"))
print(emp.get("salary"))
print(emp.get("empname"))
print(emp.get("color"))
print(emp.get("marks"))
print(emp.get("loc"))


print(emp.keys())

for key  in emp.keys():
    print(key ,"  Value is =>  " ,emp.get(key))
'''