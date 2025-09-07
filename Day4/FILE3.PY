text="Welcome to Python programming"

for ch in text:
    print(ch,end='')

print()
print(text.replace("Python","Java"))
print(text.split())

print("------------------")

list=text.split()

for i in list:
    print(i.upper())


print("one,two,three".split(",")) 


'''

print(text.find("Python"))   # 7 (index position)
print(text.find("Java"))     # -1 (not found)
print(text.index("Python"))  # 7 (error if not found)
print(text.startswith("We"))# True
print(text.endswith("g"))  # True
print(text.count('Python'))

print(text.upper())     # HELLO PYTHON
print(text.lower())     # hello python
print(text.title())     # Hello Python
print(text.capitalize())# Hello python
print(text.swapcase())  # hELLO pYTHON

print(text.strip().upper())     # "Hello Python" (removes spaces both sides)
print(text.lstrip())    # "Hello Python " (removes left spaces)
print(text.rstrip())    # " Hello Python" (removes right spaces)
'''