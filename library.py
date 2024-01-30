

class Book:

    def __init__(self, title, author, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    
    def make_available(self):
        self.is_available = True
    def make_unavailable(self):
        self.is_available = False
    def get_available(self):
        return self.is_available
    
    def get_isbn(self):
        return self.isbn
    
    def __str__(self):
        return f"{self.title} by {self.author}. {'AVAILABLE' if self.is_available else 'UNAVAILABLE'}"



class DigitalBook(Book):

    def __init__(self, title, author, isbn: str, compatible_format: str):
        super().__init__(title, author, isbn)
        self.compatibilities = set(compatible_format)

    def add_compatibility(self, compatibility: str):
        self.compatibilities.add(compatibility)
        
    def make_unavailable(self):
        # Override super method to make sure digital books are alwyas available
        pass

    def __str__(self):
        out = super().__str__()
        return out + " - DIGITAL"



class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        book.make_available()
        self.books.append(book)

    def borrow_book(self, isbn: str) -> Book:
        for book in self.books:
            if book.get_isbn() == isbn:
                if book.get_available():
                    book.make_unavailable()
                    return book
                else:
                    print("Book unavailable.")
        print("Book does not exist in library.")

    def __str__(self):
        out = ""
        for book in self.books:
            out += str(book) + '\n'
        return out



def main():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    dbook1 = DigitalBook("1984", "George Orwell", "978-0451524935", "Kindle")
    library = Library()
    print(library)
    library.add_book(book1)
    library.borrow_book("978-0451524935")
    library.add_book(book2)
    library.borrow_book("978-0451524935")
    library.add_book(dbook1)
    library.borrow_book("978-0451524935")
    library.borrow_book("978-0451524935")
    print(library)

main()