class books:
    def __init__(self, title, author, isbn, is_avilable=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_avilable = is_avilable

    def describe(self):
        return f"Title: {self.title}, Author: {self.author}"


class library:
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

        if book and book.is_avilable:
            book.is_avilable = False
            return f"Book '{book.title}' checked out successfully."

        elif book:
            return f"Book '{book.title}' is not available for checkout."

        else:
            return "Book not found in the library."

    def return_book(self, isbn):
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
    def __init__(self, file_size_mb, title, author, isbn, is_avilable=True):
        super().__init__(title, author, isbn, is_avilable)

        self.file_size_mb = file_size_mb

    def describe(self):
        return f"Title: {self.title}, File Size: {self.file_size_mb} MB"


def is_valid_isbn(isbn):
    return len(isbn) == 13 and isbn.isdigit()


def available_books(library):
    return list(filter(lambda book: book.is_avilable, library))


def sort_books(library):
    return sorted(library, key=lambda book: book.title)


def all_books(library):
    return list(map(lambda book: book.title, library))


if __name__ == "__main__":

    my_library = library()

    book1 = books("Python Basics", "Ahmed", "1111111111111")
    book2 = books("Clean Code", "Robert", "2222222222222")
    book3 = EBook(10, "FastAPI", "Ali", "3333333333333")
    book4 = EBook(15, "Django", "Omar", "4444444444444")
    book5 = books("Algorithms", "Hassan", "5555555555555")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4)
    my_library.add_book(book5)

    print(my_library.checkout_book("1111111111111"))
    print(my_library.return_book("2222222222222"))

    book_list = [book1, book2, book3, book4, book5]

    print("Available Books:")
    for book in available_books(book_list):
        print(book.describe())

    print("Sorted Books:")
    for book in sort_books(book_list):
        print(book.describe())

    print("All Titles:")
    print(all_books(book_list))