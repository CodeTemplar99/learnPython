age = 22
if age > 18:
    print("eligible")
elif age < 18:
    print("not eligible")


# this code can be reformated to look like

if age > 18:
    message = "eligible"
elif age < 18:
    message = "not eligible"
print(message)


# with tenary operators this can be rewritten as
message = "eligible" if age >= 18 else "not eligible"
print(message)
