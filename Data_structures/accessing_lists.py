# to access an item in a list use the square bracket notation
letters = ["a", "b", "c", "d"]
# to get the letter "c" in the letters list
print(letters[2])
# prints "c"

# change the value of a list
letters[0] = "A"
print(letters[0])
# prints an uppercase letter A

# accessing lists by index
# prints the first character
print(letters[0])
# prints from the first character to the last
print(letters[0:])

# prints from the first character to the 3rd
print(letters[0:2])

# prints from the first character to the 5th
print(letters[:4])

numbers = list(range(21))
# prints the second item from the back
print(numbers[-1])

# reverses the original list from the back
print(numbers[::-1])

# skipped items by 2
print(numbers[::2])

# skipped items by 3
print(numbers[::3])
