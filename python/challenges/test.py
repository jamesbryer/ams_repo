def load_valid_words(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)


def find_longest_subwords(input_str, valid_words):
    input_str = input_str.lower()
    result = []
    word = ""
    last_valid_position = -1

    for i, char in enumerate(input_str):
        word += char
        if word in valid_words:
            last_valid_position = i
        elif last_valid_position != -1:
            result.append(input_str[:last_valid_position + 1])
            input_str = input_str[last_valid_position + 1:]
            word = ""
            last_valid_position = -1

    if word:  # In case the last word is valid
        result.append(word)

    return result


if __name__ == "__main__":
    # Replace 'path/to/your/wordlist.txt' with the actual path to your wordlist file.
    wordlist_file = 'python/challenges/list_of_words.txt'
    valid_words = load_valid_words(wordlist_file)

    input_str = input("Enter a string: ")
    subwords = find_longest_subwords(input_str, valid_words)
    print("Sub-words:", subwords)
