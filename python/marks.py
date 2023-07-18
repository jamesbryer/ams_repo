mark = input("Enter your mark: ")

if mark.isdigit():
    mark = int(mark)
    if mark > 100:
        print("Wow you're literally goated")
    elif mark >= 85:
        print("Distinction")
    elif mark >= 65:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not a valid mark")

# now the same code but without using elif
mark = input("Enter your mark: ")

if mark.isdigit():
    mark = int(mark)
    if mark > 100:
        print("Wow you're literally goated")
    if mark >= 85 and mark <= 100:
        print("Distinction")
    if mark >= 65 and mark < 85:
        print("Pass")
    if mark < 65:
        print("Fail")
else:
    print("Not a valid mark")
