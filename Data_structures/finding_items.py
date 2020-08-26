letters = ["a", "b", "c", "d", "e", "f", "g"]
# this prints the index of the passed character
print(letters.index("c"))

# when you try to print a character that is not in the list,
# python will throw an error
# most programming languages will return a negative 1
# to prevent throwing error while trying to get an index in a list
if "X" in letters:
    print(letters.index("X"))
# this prints nothing because it is false

# another useful way is to use count to get the number of occurrences
print(letters.count("W"))
# prints 0
