'''
def square(x):
    return x * x

def display_result(y):
    result = square(y)
    print("Result:", result)

#function call
display_result(6)
'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(10))  # Output: 120