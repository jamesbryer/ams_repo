# function for calculation factorial of a number
# using type hints for function arguments and return value
def factorial(n: int) -> int:
    # docstring for function: stored in __doc__ attribute
    '''
    factorial(n): Calculates factorial of a number
    '''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# if this file is run directly, run the following code - prevents code from running if imported
if __name__ == '__main__':
    num = factorial(5)
    print("I love", num)

# use python3 -m pydoc -w doc_example to generate documentation for this file CD TO SAME DIRECTORY!!!
# in the interpreter, can use help(doc_example) to see the documentation after importing the module using from doc_example import factorial
