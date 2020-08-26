# a filter function is used to filter a list of items: it takes two parameter a funnction or none and an iterable
# the result of the function is a boolean value so if it is true the value is returned
# we then pass the list (to be sorted as the second parameter)
items = [
    ("product1", 10),
    ("product2", 43),
    ("product3", 7),
    ("product4", 4),
    ("product5", 23),
    ("product6", 9),
    ("product7", 1),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
