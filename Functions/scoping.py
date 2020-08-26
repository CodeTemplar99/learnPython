# a scope is an area where a variable is accessible
# variables can be defined in the:
# global scope: where it is accessible across all parts of the code
# local scope: where it is limited only to a region of the code
# when scoping in functions, the indentation determines whether an object/variable is in the function scope or not
# when an object/variable is not within the function's indentation it is outside the
# scope, the opposite for when it is in the function scope


# example of global scoping

# this variable is defined outside of any function so it is accessible across this
# scoping.py file
course = "python"


def print_course():
    # this code below accesses the course variable successfully

    # this prints global variable course //python
    print(course)


print_course()


# local scoping

def print_course1():
    # not minding that course variable already exists in the global scope
    # this definition below is also good and it will not affect the global
    # variable because the are not familiar with eachother
    # this course variable exists only in this function block
    course = "python course"
    # this will print the value of course in this function block
    print(course)


# call the print_course1 function
print_course1()

# printing course anywhere in this code will return the value of the global scopped function


# to modify the value of a global scoped function in a local scope
# NOTE: this is a bad practice, if there are other variables depending on the global
# function that has been modified, this may affect the code adversely...leading to bugs
def modify_course_global_value():
    global course
    course = "python made easy course"
    # this will print the modified value of the global course in this function block
    print(course)


# call the modify_course_global_value function
modify_course_global_value()

# this prints the modified course value
print(course)
