# number of parametres must equal the number of arguments
# In a situation when a developer wants to work with more than one arguments,
# he can pass in a variable of arguments

# this is achieved using an asterix or a start before the parametre name
# it is always better to use parameters that appear in this form in plural
def multiply(*numbers):
    total = 1
    # since this is a list of parameters now, it is now iterable therefore
    # number in numbers stands means any single item in the list
    for number in numbers:
        total *= number
    return total
    # the return is placed in the same indention with the for loop not inside to avoid #printing singlary


print(multiply(2, 3, 4, 5, 6))
# this code will print the values of the progressive multiplication of the listed numbers
# 720
