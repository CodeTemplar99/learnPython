items = [
    ("product1", 10),
    ("product2", 43),
    ("product3", 7),
    ("product4", 4),
    ("product5", 23),
    ("product6", 9),
    ("product7", 1),
]

# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

# instead of using the above commented code, we can use a map function
# the map function will pass a lambda function aon every single item in the list
# the map function takes two parametres: thefunction and iterables
x = map(lambda item: item[1], items)
# the map function returns a map object which is iterable
# then loop over it and print every item
for item in x:
    print(item)
