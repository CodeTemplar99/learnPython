# a dictionary is a key-value pair list of items
# dictionary can be defined by:
point = {"x": 1, "y": 2}
# NOTE the key can be of any data type but strings are convectional

# a dictionary can be defined by
point = dict(x=1, y=2)
# we can modify a dictionary
# change value
point["x"] = 10
# add a new item
point["z"] = 20

# when you call an invalid key you get an error to prevent this
# check for a key
if "a" in point:
    # this won't print
    print(point["a"])
# another way is
print(point.get("a", 0))
# the above code will return none but you can pass a default item to be displayed if
# the item doesn't in the dictionary

# you can loop over a dictionary
for x in point:
    print(x)

# or

for x in point.items():
    print(x)
# above code prints a topple

# the code below gets they key and the value and prints it
for key, value in point.items():
    print(key, value)
