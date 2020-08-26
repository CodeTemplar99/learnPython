# lambda function are anonymmus functions that we use once in another function
# they are simpler formatted functions
# the syntax is
# lambda parameters: expression
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

# def sort_items(item):
#     return item[1]


# items.sort(key=sort_items)
# print(items)

# instead of using the commented codes above with lambda it can be written as
items.sort(key=lambda item: item[1])
print(items)
