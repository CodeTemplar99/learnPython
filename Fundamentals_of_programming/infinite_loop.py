# an infinite loop is an endless loop that will continue
# infinite loops useful when they are managed well but they  can cause major memory consumption if not properly managed

# example of a command review built on infinite loop

while True:
    command = input("Enter a command: ")
    print(">>>" + " " + command)
    if command.lower() == "quit":
        break
print("hello, the app stopped because you called quits")


# in the above program the while will always evaluate to true thereby making the program to be able to run as long as possible.
# this can be check when a command equals quit thereby invoking the break statement on the loop
# this in turn does not affect the truthiness of the while loop
