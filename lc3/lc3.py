class books:
    def __init__(self, title , author , isbn , is_avilable = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_avilable = is_avilable

    def describe(self):
        return f"Title: {self.title}, Author: {self.author},"
class library:
    def __init__(self):
        self.__books= []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        self.__books.remove(book)

    def find_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                return book
        return None

    def checkout_book(self,isbn):
        book = self.find_book(isbn)
        if book and book.is_avilable:
            book.is_avilable = False
            return f"Book '{book.title}' checked out successfully."
        elif book:
            return f"Book '{book.title}' is not available for checkout."
        else:
            return "Book not found in the library."

    def return_book(self,isbn):
        book = self.find_book(isbn)
        if book:
            book.is_avilable = True
            return f"Book '{book.title}' returned successfully."
        else:
            return "Book not found in the library."

    def list_available_books(self):
        available_books = []

        for book in self.__books:
            if book.is_avilable:
                available_books.append(book)

        return available_books
    

class EBook(books):
    def __init__(self,file_size_mb, title , author , isbn , is_avilable = True):
        super().__init__(title , author , isbn , is_avilable)
        self.file_size_mb = file_size_mb
    def describe(self):
        return f"Title: {self.title},File Size: {self.file_size_mb} MB"