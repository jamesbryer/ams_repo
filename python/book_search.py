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
    "Oscar Wilde": ["The Picture of Dorian Gray", "The Importance of Being Earnest"],
    "J. K. Rowling": ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince", "Harry Potter and the Deathly Hallows"]
}

# ask the user for an author's name
authorName = input("Please enter the author's name: ")
# check if the author is in the dictionary
if authorName not in books.keys():
    print("Sorry, we don't have any books by", authorName)
else:
    # print the books by the author
    print("The following books are written by", authorName + ":")
    print(', '.join(sorted(books[authorName])))
