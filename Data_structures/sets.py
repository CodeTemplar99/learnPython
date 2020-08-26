# sets are unordered collection of unique items
# much like the list, sets can be manipulated but can not be indexed
# i.e the items can not be gotten by their index, trying to do this will throw an error
# sets are powerful because of their mathematical poweress
numbers = [1, 2, 3, 4, 4, 5, 5]
first = set(numbers)
# this prints the set without a repetition
print(first)

second = {1, 6}

# union of sets
print(first | second)

# compliment of sets
print(first & second)

# difference of sets
print(first | second)

# symmetric difference - items that are either of the given sets but not in both
print(first | second)
