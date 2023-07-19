def multiply(list):
    product = 1
    for i in list:
        product *= i
    return product


print(multiply([8, 2, 3, -1, 7]))
