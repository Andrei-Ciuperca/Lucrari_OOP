class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book with ISBN {isbn} not found in the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"'{book.title}', written by: '{book.author}', ISBN: {book.isbn}")

book1 = Book("Cat's Eye", "Margaret Atwood", "9780385491020")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

library = Library()
library.add_book(book1)
library.add_book(book2)
print("------------------------")
library.display_books()
print("------------------------")
library.remove_book("9780385491020")
print("------------------------")
library.display_books()