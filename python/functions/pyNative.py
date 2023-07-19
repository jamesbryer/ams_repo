# write a function which can accept any number of arguments

def manyArgs(*args):
    for arg in args:
        print(arg)


manyArgs(1, 2, 3, 45, 3, 234, 4, 3, "cheese")

# write a function that returns multiple values (calcs both addtion and subraction)


def addAndSubtract(a, b):
    add = a + b
    sub = a - b
    return add, sub


add, sub = addAndSubtract(5, 7)
print(add, sub)

# write a function with a default argument


def nameAndSalary(name, salary=9000):
    print("Name:", name, "Salary:", salary)


nameAndSalary("James")

# write an inner function within a function


def addFive(a, b):

    def addTwo(a, b):
        return a + b

    add = addTwo(a, b)

    return add + 5


res = addFive(5, 5)
print(res)

# write a function to be reassigned and call it with a different name


def nameAge(name, age):
    print(name, age)


# use assignment to copy function into another name
nameAgeTwo = nameAge
nameAgeTwo("james", 25)

# write a function to generate all the even numbers between two values


def printEven(a, b):
    print(list(range(a, b, 2)))


printEven(4, 30)

# write a function to find the largest number in a list


def largetNum(list):
    return max(list)


lrg = largetNum([1, 3, 5, 3, 2342345, 654, 3453423, 4, 4, 9, 43245345635])
print(lrg)
