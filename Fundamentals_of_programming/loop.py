# loops  are used to perform an action repeatedly

# printing a message thrice
for number in range(3):
    print("attempt")
print("\n")


# printing a message thrice and addingthe count
for number in range(3):
    print("attempt", number)
print("\n")

# printing a message thrice and adding a number to the count
for number in range(3):
    print("attempt", number + 1)


# printing a message thrice and adding a number to the count and increasing a dot ny the count number
for number in range(3):
    print("attempt", number + 1, (number + 1) * ".")
print("\n")


# printing a message thrice and adding a number to the count and increasing a dot ny the count number
# manipulating the range method
for number in range(0, 4):
    print("attempt", number + 1, (number + 1) * ".")
print("\n")


# printing a message thrice and adding a number to the count and increasing a dot ny the count number
# manipulating the range method: starting from behind 0, stopping before 9 and jumping 3 numbers
for number in range(1, 9, 2):
    print("attempt", number, number * ".")
print("\n")
