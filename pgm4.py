class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.available=True

    def borrow(self):
        if self.available:
            self.available = False
            print(f" '{self.title}' Borrowed")
        else:
            print(f" '{self.title}' Not Available")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f" '{self.title}' Returned")
        else:
            print(f"'{self.title}' not borrowed")
    def __str__(self):
        if self.available:
            status = "Available"
        else:
            status = "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added")

    def display_books(self):
        print("Available Books")
        for book in self.books:
            if book.available:
                status = "Available" 
            else:
                status="Borrowed"
            print(f"Title: '{book.title}', Author: '{book.author}', Status: '{status}'")
        print()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return
        print("Book '{title}' Not Found")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print("Book '{title}' Not Found.")


if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("The God of Small Things", "Arundhati Roy"))
    lib.display_books()
    lib.borrow_book("The God of Small Things")
    lib.return_book("The God of Small Things")
        