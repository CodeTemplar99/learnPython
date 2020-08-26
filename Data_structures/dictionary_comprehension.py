# a dictionary comprehension expression is used to create a propagatory dictionary

# for example instead of doing
values = {}
for x in range(5):
    values[x] = x * 2

print(values)


# we can have something like
values = {x: x * 2 for x in range(5)}
print(values)

# the above code can be used to create a list(list comprehension expression) but NOT a topple
