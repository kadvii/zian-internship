class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def describe(self):
        return f"Title: {self.title}, Author: {self.author}"


class EBook(Book):
    def __init__(self, title, author, isbn, file_size_mb, is_available=True):
        super().__init__(title, author, isbn, is_available)
        self.file_size_mb = file_size_mb

    def describe(self):
        return (
            f"Title: {self.title}, Author: {self.author}, "
            f"File Size: {self.file_size_mb} MB"
        )


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        self.__books.remove(book)

    def find_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                return book

        return None

    def checkout_book(self, isbn):
        book = self.find_book(isbn)

        if book and book.is_available:
            book.is_available = False
            return f"Book '{book.title}' checked out successfully."

        if book:
            return f"Book '{book.title}' is not available for checkout."

        return "Book not found in the library."

    def return_book(self, isbn):
        book = self.find_book(isbn)

        if book:
            book.is_available = True
            return f"Book '{book.title}' returned successfully."

        return "Book not found in the library."

    def get_available_books(self):
        return list(filter(lambda book: book.is_available, self.__books))

    def get_sorted_books(self):
        return sorted(self.__books, key=lambda book: book.title)

    def get_titles(self):
        return list(map(lambda book: book.title, self.__books))


def is_valid_isbn(isbn):
    return len(isbn) == 13 and isbn.isdigit()
