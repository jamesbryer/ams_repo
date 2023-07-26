# <QUESTION 1>

# Given a word and a string of characters, return the word with all of the given characters
# replaced with underscores

# This should be case sensitive

# <EXAMPLES>

# one("hello world", "aeiou") → "h_ll_ w_rld"
# one("didgeridoo", "do") → "_i_geri___"
# one("punctation, or something?", " ,?") → "punctuation__or_something_"

def one(word, chars):
    replaced_string = ''
    for char in word:
        if char in chars:
            replaced_string += "_"
        else:
            replaced_string += char
    return replaced_string


# <QUESTION 2>

# Given an integer - representing total seconds - return a tuple of integers (of length 4) representing
# days, hours, minutes, and seconds

# <EXAMPLES>

# two(270) → (0, 0, 4, 30)
# two(3600) → (0, 1, 0, 0)
# two(86400) → (1, 0, 0, 0)

# <HINT>

# There are 86,400 seconds in a day, and 3600 seconds in an hour


def two(total_seconds):

    units = [86400, 3600, 60, 1]
    result = []
    remaining = total_seconds
    for unit in units:
        this_unit = int(remaining / unit)
        remaining = remaining % unit
        result.append(this_unit)
    result = tuple(result)
    return result


# <QUESTION 3>

# Given a dictionary mapping keys to values, return a new dictionary mapping the values
# to their corresponding keys

# <EXAMPLES>

# three({'hello':'hola', 'thank you':'gracias'}) → {'hola':'hello', 'gracias':'thank you'}
# three({101:'Optimisation', 102:'Partial ODEs'}) → {'Optimisation':101, 'Partial ODEs':102}

# <HINT>

# Dictionaries have methods that can be used to get their keys, values, or items


def three(dictionary):

    swapped_dict = {value: key for key, value in dictionary.items()}

    return swapped_dict

    # <QUESTION 4>

    # Given an integer, return the largest of the numbers this integer is divisible by
    # excluding itself

    # This should also work for negative numbers

    # <EXAMPLES>

    # four(10) → 5
    # four(24) → 12
    # four(7) → 1
    # four(-10) → 5


def four(number):

    # convert to absolute number so negative integers work
    number = abs(number)
    if number == 1:
        return 1
    # this biggest factor cannot be larger than half the original, so save some compute
    divisible = int(number / 2)

    # iterate through all numbers until the highest factor is found
    while divisible > 0:
        if number % divisible == 0:
            return divisible
        divisible -= 1

    # <QUESTION 5>

    # Given a string of characters, return the character with the lowest ASCII value

    # <EXAMPLES>

    # five('abcdef') → 'a'
    # four('LoremIpsum') → 'I'
    # four('hello world!') → ' '


def five(chars):
    # using comprehension to set ASCII value as key and character as value in the dictionary
    dict = {ord(char): char for char in chars}
    highest = dict[min(dict.keys())]
    return highest

    # <QUESTION 6>

    # Given a paragraph of text and an integer, break the paragraph into "pages" (a list of strings), where the
    # length of each page is less than the given integer

    # Don't break words up across pages!

    # <EXAMPLES>

    # six('hello world, how are you?', 12) → ['hello world,', 'how are you?']
    # six('hello world, how are you?', 6) → ['hello', 'world,', 'how', 'are', 'you?']
    # six('hello world, how are you?', 20) → ['hello world, how are', 'you?']


def six(paragraph, limit):
    words = paragraph.split()  # Split the paragraph into individual words
    pages = []
    current_page = []

    for word in words:
        if len(" ".join(current_page + [word])) <= limit:
            current_page.append(word)
        else:
            pages.append(" ".join(current_page))
            current_page = [word]

    # Add the last remaining page, if any
    if current_page:
        pages.append(" ".join(current_page))

    return pages


if __name__ == "__main__":

    # test function 1
    print(one("hello world", "aeiou"))
    print(one("didgeridoo", "do"))
    print(one("punctation, or something?", " ,?"))

    # test function 2
    print(two(270))
    print(two(3600))
    print(two(86400))

    # test function 3
    print(three({'hello': 'hola', 'thank you': 'gracias'}))

    # test function 4
    print(four(10))
    print(four(24))
    print(four(7))
    print(four(-10))

    # test function 5
    print(five('abcdef'))
    print(five('LoremIpsum'))
    print(five('Hello World'))

    # test function 6
    print(six('hello world, how are you?', 12))
