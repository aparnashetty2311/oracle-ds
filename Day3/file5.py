def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()
    print("Outer function")
    inner()
    print("Outer function")
    inner()
    
print("Outer function")
outer()

