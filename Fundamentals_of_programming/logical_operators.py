# AND
# this aims to meet the condition of two conditions in other to execute a dependent block of code

# a loan app example

# AND
high_income = True
good_credit = True
if high_income and good_credit:
    print("eligible")
else:
    print("not eligible")

# OR
# this operators aims to meet either of both set set conditions
high_income = True
good_credit = False
if high_income or good_credit:
    print("eligible")
else:
    print("not eligible")

# NOT
# this negates the given value to achieve it's aim
high_income = True
good_credit = True
student = True
if not student:
    print("eligible")
else:
    print("not eligible")


# combining "and" ,"or" and "and"
high_income = True
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("not eligible")
