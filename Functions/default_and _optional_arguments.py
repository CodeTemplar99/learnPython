# functions have default parameters
# this means that when ever a function is called it must have it's argument equal to the
# number of parameters
# example of default argument
def increment(number, by):
    return number + by


    # when this is called the number of arguments must be equal to the number of parameters
print(increment(2, by=3))
# this will print 5

# to set optional argument, we simply define the parameter with a value
# example


def increment1(number, by=3):
    return number + by


print(increment1(2))
# this will print 5

# NOTE: the required argument is a parameter that is not defined with value
# NOTE: optional argument is a parameter that is defined with value when defining the function
# NOTE: the optional argument in this case 3 should not come before any required argument(s)
# NOTE: the optional argument always comes last
