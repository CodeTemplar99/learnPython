#
try:
    age = int(input("Age:"))
    x_factor = age // 10
# **ZeroDivisionError is gotten when you try to divide a number by zero(0) in python

except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")

# this code below will not be executed because it has been matched on line 5, thereby making
# the line below redundant
except ZeroDivisionError:
    print("you didn't enter a valid age")
else:
    print("no exception caught")
