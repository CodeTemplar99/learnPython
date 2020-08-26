# unpacking operators are used to unpack individual items in an iterable
# example
# to print a list of numbers singly e.g 1 2 3 4
# we can do
numbers = [1, 2, 3, 4, 5]
# unpacking operator before the iterable
print(*numbers)
# we can have something like
numbers = [*range(6)]
print(*numbers)

# we can unpack a list too

# to unpack a dictionary, used double asterix

first = dict(x=1)
second = dict(x=10, y=2, z=3)
combined = {**first, **second}
print(combined)

# NOTE: when two key-pair value are present the last one will be choosed
print(divmod(100, 50))
