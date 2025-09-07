words = ["I", "love", "Python"]  # List 
print(words)
print(" ".join(words))   # I love Python

test=" ".join(words)
print(test.split())


s = "Python3"
print(s.isalpha())   # False (contains digit)
print("Python".isalpha())  # True
print(s.isdigit())   # False
print("12345".isdigit())   # True
print(s.isalnum())   # True (letters+digits)
print(" ".isspace()) # True
