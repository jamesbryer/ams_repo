def valid_isbn_13(isbn):
    isbn = isbn.replace("-", "")
    count = 1
    isbn_list = []
    checksum = int(isbn[-1])
    isbn = isbn[:-1]

    for digit in isbn:
        if count % 2 == 0:
            isbn_list.append(int(digit) * 3)
        else:
            isbn_list.append(int(digit) * 1)
        count += 1

    isbn_list = [int(x) for x in isbn_list]
    check_sum = 10 - (sum(isbn_list) % 10)
    print(check_sum)
    if check_sum == checksum:
        return True
    else:
        return False


isbn = "978-0-00-821843-0"
checksum = valid_isbn_13(isbn)
print("Checksum for ISBN-13", isbn, "is:", checksum)
