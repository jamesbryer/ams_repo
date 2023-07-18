# initialise a dictionary of classic books with their authors
books = {
    "Charles Dickens": ["A Christmas Carol"],
    "William Shakespeare": ["Hamlet", "Macbeth", "Romeo and Juliet"],
    "Mark Twain": ["Adventures of Huckleberry Finn", "The Adventures of Tom Sawyer"],
    "Jane Austen": ["Pride and Prejudice", "Emma", "Sense and Sensibility"],
    "Arthur Conan Doyle": ["The Adventures of Sherlock Holmes", "The Hound of the Baskervilles"],
    "Lewis Carroll": ["Alice's Adventures in Wonderland", "Through the Looking-Glass"],
    "Jules Verne": ["Journey to the Center of the Earth", "Twenty Thousand Leagues Under the Sea"],
    "Charlotte Bronte": ["Jane Eyre"],
    "Emily Bronte": ["Wuthering Heights"],
    "Oscar Wilde": ["The Picture of Dorian Gray", "The Importance of Being Earnest"]
}

# ask the user for an author's name
authorName = input("Please enter the author's name: ")
# check if the author is in the dictionary
if authorName not in books.keys():
    print("Sorry, we don't have any books by", authorName)
else:
    # without looping through the dictionary, we can use the .get() method to get the value of the key
    print("The following books are written by", authorName + ":")
    print(', '.join(books[authorName]))
