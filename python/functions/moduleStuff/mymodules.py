def sumList(list):
    sum = 0
    for i in list:
        if type(i) == int or type(i) == float:
            sum += i
        else:
            continue
    return sum


def maxOfThree(a, b, c):
    list = [a, b, c]
    list.sort()
    return list[2]


def factorial(value):
    if value == 1:
        return 1
    else:
        return value * factorial(value - 1)


def multiply(list):
    product = 1
    for i in list:
        product *= i
    return product


def mrShouty(string):
    return string.upper()


def addFive(number: float):
    return number + 5


def len():
    return "hi i am len"
