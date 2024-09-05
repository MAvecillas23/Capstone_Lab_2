# This program creates a class object named Author that holds the authors name and a list of books published

class Author:

    # Creates the author object with the authors name as a parameter
    # and creates an empty books list that holds books published
    def __init__(self, name):
        self.name = name
        self.books = []

    # everytime publish is called with a book title, the title is added to the empty books list
    def publish(self, book_title):
        # this if statement ensures no duplicate books are added to the author objects books list
        # if a book exists it is not added to the list and tells the user
        if book_title in self.books:
            print(f'{book_title} already exists. {book_title} was not added.')
        else:
            self.books.append(book_title)

    # displays authors name and books published to user
    def __str__(self):
        if self.books: # if there are books in the book list
            book_list = ', '.join(self.books) # join the book list
        else:
            book_list = 'No books'  # if no books in book list
            # book_list will now hold the string 'No books'
        return f'Author: {self.name}    Books: {book_list}'

# some authors and books data
orwell = Author('George Orwell')
orwell.publish('1984')
orwell.publish('Animal Farm')

shakespeare = Author('William Shakespeare')
shakespeare.publish('Hamlet')
shakespeare.publish('Romeo & Juliet')

# posting a duplicate
orwell.publish('1984')
shakespeare.publish('Hamlet')

# display to user
print(shakespeare)
print(orwell)

# part 3 - In my opinion, working with dataclasses is a bit more simple when creating instance variables as opposed to
# with regular classes you have to create an initializer with a function and parameters and instance variables...
# dataclasses creates a simpler way to display data to the user with legible code unless you overwrite the type of string you'd
# like to print whereas in regular classes you'll output something unreadable and it might be a bit difficult to figure out
# why output is not legible