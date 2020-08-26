# a zip function is used to add to or more lists together and print it as a topple
# map and list comprehension cannot work in this scenario because it works for only one list

list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]

# this function takes 2 or more iterables
print(list(zip(list1, list2)))

# cool stuff
# you can add strings too
print(list(zip("abc", list1, list2)))
