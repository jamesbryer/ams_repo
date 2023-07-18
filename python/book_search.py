# initialise a dictionary of classic books with their author as keys including all the harry potter books
books = {
    "The Hitchhiker's Guide to the Galaxy": "Douglas Adams",
    "The Lord of the Rings": "J. R. R. Tolkien",
    "The Cat in the Hat": "Dr. Seuss",
    "The Very Hungry Caterpillar": "Eric Carle",
    "Charlie and the Chocolate Factory": "Roald Dahl",
    "Charlotte's Web": "E. B. White",
    "The Hobbit": "J. R. R. Tolkien",
    "The Little Prince": "Antoine de Saint-Exupéry",
    "Harry Potter and the Philosopher's Stone": "J. K. Rowling",
    "Harry Potter and the Chamber of Secrets": "J. K. Rowling",
    "Harry Potter and the Prisoner of Azkaban": "J. K. Rowling",
    "Harry Potter and the Goblet of Fire": "J. K. Rowling",
    "Harry Potter and the Order of the Phoenix": "J. K. Rowling",
    "Harry Potter and the Half-Blood Prince": "J. K. Rowling",
    "Harry Potter and the Deathly Hallows": "J. K. Rowling",
    "The Lion, the Witch and the Wardrobe": "C. S. Lewis",
    "The Secret Garden": "Frances Hodgson Burnett",
    "The BFG": "Roald Dahl",
    "Alice's Adventures in Wonderland": "Lewis Carroll",
    "Winnie-the-Pooh": "A. A. Milne",
    "The Da Vinci Code": "Dan Brown",
    "The Catcher in the Rye": "J. D. Salinger",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "The Hunger Games": "Suzanne Collins"
}

# ask the user for an author's name
authorName = input("Please enter the author's name: ")
# initialise an empty list to store the books by the author
booksByAuthor = []

# check if the author is in the dictionary
if authorName not in books.values():
    print("Sorry, we don't have any books by", authorName)
else:
    print("The following books are written by", authorName + ":")
    # loop through the books in the dictionary
    for book in books:
        # check if the author of the book is the same as the author entered by the user
        if books[book] == authorName:
            # add the book to the list of books by the author
            booksByAuthor.append(book)
    # sort the list of books alphabetically
    booksByAuthor = sorted(booksByAuthor)
    # print the list of books
    print(', '.join(booksByAuthor))
