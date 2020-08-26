successful = True
for number in range(3):
    print("attempt", number + 1, (number + 1) * ".")
    if successful:
        print("successful!!!")
        print("\n")
        break
        print("hello")
else:
    print("not successful")

# this codes stops on reaching the break statement on line 6 thereby making the print statement of line 7 unreachable i.e redundant


successful = False
for number in range(3):
    print("attempt", number + 1, (number + 1) * ".")
    if successful:
        print("successful!!!")
        break
else:
    print("not successful")
