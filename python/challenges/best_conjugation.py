def conjugate(word):
    with open("python/challenges/list_of_words.txt") as file:
        lines = file.readlines()
        lines = {line.strip() for line in lines}

    test = ""
    words = []
    for char in word:
        test += char
        if test in lines:
            current_word = test
            for j in word:
                if current_word + j in lines:
                    current_word += j
                else:
                    break
            words.append(current_word)

    return words


# Example usage:
words = conjugate("awesomeness")
print(words)
