# to add or remove objects in a list we call a method on it
# a methos is an individual function that is part of an object

# ADD
letters = ["a", "b", "c", "d", "e", "f", "g"]
# to add at the end of a list
letters.append("X")

# to add in a position
# here 0 is the position and "XX" the character to append
letters.insert(0, "XX")
print(letters)

# REMOVE
# removes the last item
letters.pop()
# removes the item with the given index
letters.pop(0)
# this will remove the first occurrence of the passed character
# to remove all characters write a loop
letters.remove("b")
# deletes a group of items
del letters[0:3]

# to clear all items
letters.clear()
print(letters)
