# an argument is a value passed when calling a function

def increment(number, by):
    return number+by


value = increment(2, 1)
print(value)

# the above code will return 3


# to simplify this it can be written as

def increment2(number, by):
    return number + by


# value2 = increment2(2, 2)
print(increment2(2, 2))

# the above code prints 4
#  now because the use of "value2" will be infinitesimal or negligible because it's used once
#  it can be replaced by calling the increment with arguments inside the print function
# but this will made the code less understandable.
# this means as the parameters and arguments increase we may loose track of what what is
# to check for this we use keyword arguments


# KEYWORD ARGUMENTS
# this is by definition as the name implies: it is passing a key word to an argument
# this makes the code almost like simple english and increases readability and maintenace

def increment3(number, by):
    return number + by


print(increment3(2, by=3))

# the above code prints 5
