from library import Book, EBook, Library, is_valid_isbn


my_library = Library()

book1 = Book("Python Basics", "Ahmed", "1111111111111")
book2 = Book("Clean Code", "Robert", "2222222222222")
book3 = EBook("FastAPI", "Ali", "3333333333333", 10)
book4 = EBook("Django", "Omar", "4444444444444", 15)
book5 = Book("Algorithms", "Hassan", "5555555555555", False)

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.add_book(book5)

print(my_library.checkout_book("1111111111111"))
print(my_library.return_book("5555555555555"))

print("\nAvailable Books:")
for book in my_library.get_available_books():
    print(book.describe())

print("\nSorted Books:")
for book in my_library.get_sorted_books():
    print(book.describe())

print("\nMapped Titles:")
print(my_library.get_titles())

print("\nISBN Validation:")
print(is_valid_isbn("1111111111111"))
print(is_valid_isbn("12345"))
