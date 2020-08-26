# defining multiple variables or assign list items to different variables
numbers = [1, 2, 3, 4, 6, 7]
# first, second, third = numbers
# this will assign the first second and third list items to the defined variables

# packing variables
# in a situation when the number of list items is more than the required variables
# it is possible to select a few needed items

numerals = [1, 2, 3, 4, 6, 7]
one, two, three, *others = numerals
print(one)
print(others)

# NOTE: others is arbitrary


# to select from position e.g first and last
one, *others, last = numerals
print(last)
