# SORTING LISTS
numbers = [43, 90, 7, 22, 56, 3]
print(numbers)

# sorting
numbers.sort()
# this returns the list sorted in increasing value
print(numbers)


numbers.sort(reverse=True)
# this returns the list sorted in decreasing value using the key-word argument
print(numbers)

# another method
# this changes the original list
sorted(numbers, reverse=True)
print(numbers)

# sorting topples
# topples are like lists but they are READONLY

items = [
    ("product1", 10),
    ("product2", 43),
    ("product3", 7),
    ("product4", 4),
    ("product5", 23),
    ("product6", 9),
    ("product7", 1),
]

# here a function is defined to sort the items with the item iteration passed as a parametre
# the function returns the 1st item


def sort_items(item):
    return item[1]


# the sort method is called on the items and the key-word argument is the key and the defined function
items.sort(key=sort_items)
print(items)
