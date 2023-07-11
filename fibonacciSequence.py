# def function to generate fibonacci sequence with a given length
def fibonacciSequence(length):
    # initialize the sequence with the first two numbers
    sequence = [0, 1]
    # loop until the sequence is the desired length
    while len(sequence) < length:
        # append the sum of the last two numbers to the sequence
        sequence.append(sequence[-1] + sequence[-2])
    # return the sequence
    return sequence

# print the sequence with a length of 10
print(fibonacciSequence(10))

# define a function to put the characters of a string in alphabetical order
def alphabetize(string):
    # convert the string to a list of characters
    characters = list(string)
    # sort the list of characters
    characters.sort()
    # remove duplicate characters
    characters = list(dict.fromkeys(characters))
    # return the sorted list of characters as a string
    return ''.join(characters)

# print the alphabetized string
print(alphabetize("hello world"))