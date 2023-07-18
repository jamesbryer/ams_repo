# for loops are fun. we know how they work
# but we can do some cool stuff with them
# like iterating over a list of items
# or a string
#
string = input("Please input something: ")
for character in string:
    print(character)

# create a diamond of stars
for i in range(1, 8):
    print(" " * (8 - i) + "~" * i + "~" * (i - 1))
for i in range(1, 8):
    print(" " * i + "~" * (8 - i) + "~" * (7 - i))
