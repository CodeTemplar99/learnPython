# to handle exceptions properly and prevent your program from crashing
# put the code to be executed in a try block and
# use the except block to print a friendly message for the error
try:
    age = int(input("Age:"))

    # when a above throws an exception, the code below will not be executed because the control
    # is now moved to the except block, skipping the code below the error caught
    # this text below will not print if there's an error in age
    print("oh really?")
except ValueError:
  # the valueError is type of exception
  # additional values or arguments can be passed to the except e.g
  # except ValueError as ex(for exception), error(for errors)
    print("you didn't enter a valid age")
# you can add an else statement ==> this block executes after no exception is caught
else:
    print("no exception caught")

# the code below continues after or not catching an error
print("execution continues")
