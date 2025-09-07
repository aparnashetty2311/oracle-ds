emp={ "empno":100,
     "empname":"Nageswara",
     "salary":1000.00, 
     "color":{"red","blue","yello"},
     "marks":[23,23,34,12],
     "loc":("india","usa","canada",34,33)
     }
print(emp)
'''
print(emp.keys())
print(emp.values())
print(emp.items())
emp.update({"empname":"Sudheendra","salary":3000})
print(emp)
emp.pop("loc")
print(emp)
print("-------------------")
emp.clear()
print(emp)
'''

emp.setdefault("dept","HR")
print(emp)