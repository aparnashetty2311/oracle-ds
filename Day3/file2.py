'''def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}  :->  {value}")

show_info(name="Alice", age=25, city="Paris")

def describe_person(id, **kwargs):
    print("ID:", id)
    for key, value in kwargs.items():
        print(key, ":", value)

describe_person(101, name="Bob", age=30, country="USA")


def greet(**kwargs):
    name = kwargs.get("name", "Guest")
    msg = kwargs.get("message", "Welcome!")
    print(f"Hello {name}, {msg}")

greet(name="John", message="Good Morning!")
greet()   # Uses default values



def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} => {value}")

person = {"name": "Sara", "age": 22, "city": "London"}
show_info(**person)
'''

def demo(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

demo(1, 2, 3, name="Alice", age=25)

'''
*args → Tuple (for variable positional arguments).

**kwargs → Dictionary (for variable keyword arguments).

'''