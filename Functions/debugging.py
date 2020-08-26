# debugging is a process of finding out bugs in code
# in VSCODE
# to debug click on the debug icon by the left
# click on the settings icon if you're debugging for the first time in a
# do not edit the file just save it. this will be added to thr .JSOn in the vscode folder
# select a debugging configuration from thr debugging panel
# move the cursor to the point where you want execution to pause and insert a break point with F9
# press F5 to run the up to that point
# to execute a program one at a time press F10
# to move into a block of code (function) press F11
# to skip a block of code press Shift + F11

# NOTE: it is better to put the break point inside a buggy function so that you don't run the whole code in parts before finding the problem

# an example of a buggy multiply function


def multiply(*numbers):
    print("hello Welcome")
    total = 1
    for number in numbers:
        total *= number
        # this line below is delibrately moved into the for loop to produce the wrong result
    return total


print("hello again")
print(multiply(2, 2, 2))
