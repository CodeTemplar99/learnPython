# in python and some other programing languages, there are two types of functions
# 1. functions that perform a task
# 2. functions that return a value

# example of function that performs a task

def perform_greet(greeting):
    print(f"Michael {greeting}")


perform_greet("Good morning")

# in the above code the function performs the task of printing greeting to the screen


# example of function that return a value

def say_hello(word):
    return f"Michael {word}"


message = say_hello("hello")
print(message)

# in the code above the functions return a value, this value is not limited
# to only printing, it can be changed in the future or some other action performed on it
# when a function is of the return type, the returned value have to been held in a container in form of a variable name

# the clear difference between a task performing function and a value returning function is
# calling the print function on the different function types

# example
print(perform_greet("Good morning"))
# this above will return a none type because it just performs a task, it does not hold a value at any point.

print(say_hello("hello"))
# this above returns a value which is the passed argument because it holds a value from creation. this is  not applicable in value returning function unless another function is written to do that
