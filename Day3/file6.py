
def shout(func):
    def wrapper():
        print("Calling function...")
        func()
        print("Function call complete.")
    return wrapper

@shout
def hello():
    print("Hello, world!")

hello()