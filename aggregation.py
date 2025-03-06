
class Library:
    def __init__(self, name):
        self.name = name 
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def list_book(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library1 = Library("New York Public Library")
book1 = Book("Harry Potter",  "J.k. Rowling")
book2  = Book("The Hobbit", "J.R.R tolkein")
book3 = Book("The colour of Magic","terry Practachet")

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)

print(library1.name)
#print(library1.list_book())
for book in library1.list_book():
    print(book)