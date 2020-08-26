course = "  python programming "

# change string to upper case
print(course.upper())
# change string to lower case
print(course.lower())
# capitalize start letters
print(course.title())
# strip whitespaces
print(course.strip())

# strip to the right
print(course.rstrip())

# strip to the left
print(course.lstrip())

# find the index of a string
print(course.find("gram"))

# replacing a character in a string
print(course.replace("g", "u"))

# check if word (s) exists in a string
print("g" in course)

# check if word(s) does not exist in a string
print("x" not in course)

# format a string without concatenation
print(f"A B C D E F G H")
