# arrays are like lists but they should be used when dealing a large range of values
# to use the array import the array class from the array module
from array import array

# the array methos takes two parameters
# first: typecode  a character that describes the type of data types stored in your array]
# second: a list of items
# NOTE an array can not contain different data types
numbers = array("i", [1, 2, 3, 4])

# the array has simpler manipulation methods like the list e.g remove, append, pop, insert, geting an item by index
