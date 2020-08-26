# the while loop is used to execute a code block as long as a condition remains true

number = 100
while number > 0:
    print(number)
    number = number // 2

    # the above code will continue to run as long as the number is greater than 0


# code to accept input from a user until a "quit command is initiated"
command = ""
while command.lower() != "quit":
    command = input("Enter a command ")
    print(">>>>" + " " + command)
