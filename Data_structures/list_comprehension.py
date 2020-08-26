# in python we can use map and filter functions to manipulate lists but we can write simpler
# map and filter operations with list comprehension
# the syntax is
# [expression for item in items]
# where expression is an expression and item is a single item in the list of items

# e.g
items = [
    ("product1", 10),
    ("product2", 43),
    ("product3", 7),
    ("product4", 4),
    ("product5", 23),
    ("product6", 9),
    ("product7", 1),
]


x = map(lambda item: item[1], items)
# the above code can be written in list comprehension this way
hello = [item[1] for item in items]
print(hello)

list(filter(lambda item: item[1] >= 10, items))

# the above code can be written in list comprehension this way
filtered = [item for item in items if item[1] >= 10]
print(filtered)
