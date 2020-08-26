from sys import getsizeof

values = (x * 2 for x in range(5000))
# 64 bytes
print("gen:", getsizeof(values))

values = (x * 2 for x in range(500000))
# 64 bytes still
print("gen:", getsizeof(values))


values = [x * 2 for x in range(500)]
# 2,140 bytes in memory
print("list:", getsizeof(values))


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# when we create a list using a list comprehension expression like the code below we
# will get a list of all the items in the values


values = [x * 2 for x in range(5)]
for x in values:
    print(values)

    # the above code stores the values in memory

# when you are working with a large number of values or an infinite number of values
# it will be wrong to store all the values in memory because that an inefficient memory management

# in this case we use generators
values = (x * 2 for x in range(5))
for x in values:
    print(x)

# in the above code, values is no longer a list  it is a generator object
# at each iteration it "generates" new values
# proof
print(values)

# generator objects are memory efficient because of their sizes in memory
# example on line 1


# a backdrop for generators is that you can not get the length, doing this will throw an error because you don't know how many items will be generated
