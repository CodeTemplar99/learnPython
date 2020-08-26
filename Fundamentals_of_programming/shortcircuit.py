# in python logical operators are short circuits, this means that they will break upon arriving at a condition that meets their demand
# example the and operator will stop evaluation when ever it encounters the first false, ignoring the rest of the conditions

# AND
high_income = False
good_credit = True
student = True
if (high_income and good_credit) and not student:
    print("eligible")
else:
    print("not eligible")
# this prints not eligible because of the first false encountered

# OR
high_income = True
good_credit = False
student = True
if (high_income or good_credit) or not student:
    print("eligible")
else:
    print("not eligible")
# this prints eligible because of the first true encountered


# so in conclusion logical operators are and behave like short circuits
