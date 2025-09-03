'''
def greet(*names):   # *<variable> is array format
    for name in names:
        print("Hello", name)

greet("Nameswara")
print("------------------")
greet("Nageswara","srijit","arun")


def add_numbers(*nums):
    return sum(nums)

print(add_numbers(10, 20))
print(add_numbers(5, 10, 15, 20))
'''

def introduce(title, *names):
    print("Title:", title)
    for n in names:
        print(n)

introduce("Team Members", "John", "Sara", "Mike")

