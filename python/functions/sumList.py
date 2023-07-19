def sumList(list):
    sum = 0
    for i in list:
        if type(i) == int or type(i) == float:
            sum += i
        else:
            continue
    return sum


print(sumList([1, 2, 3, 4, 5, 6, 7, 8, 9, 6, "cheese"]))
