# python has different built in data structure e.g is list
# a list is a variable that contain more than one value

# examples of lists
# list of numbers
numbers = [1, 2, 3, 4, 5]

# list of letters
letters = ["a", "b", "c", "d", "e", "f"]

# list of lists (Matrix)
matrix = [["a", "b"], ["c", "d"]]

# concatenation of lists
combined = numbers + letters
print(combined)

# multiplication of list
zeros = [0] * 10
print(zeros)

# the list in-built function can be used to make lists
location = list("madagascar")
print(location)

# to make a list of a range of values,
# this does not include the end value
numeration = list(range(20))
print(numeration)

# a string is also a list e.g
chars = list("hello I am a string but I am also a list")
print(chars)

# to print the length of a list

print(len(chars))
# prints 40 (including the spaces)
