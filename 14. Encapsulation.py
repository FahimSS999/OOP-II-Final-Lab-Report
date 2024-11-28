class LibraryBook:
    def __init__(self, isbn, title, author):
        self.__isbn = isbn
        self._title = title
        self._author = author
        self.status = "available"

    def get_ISBN(self):
        return f"ISBN: {self.__isbn[:3]}***{self.__isbn[-3:]}"

    def borrow_book(self, borrower_name):
        self.status = "borrowed"
        print(f"'{self._title}' borrowed by {borrower_name}")

    def _display_basic_info(self):
        print(f"Title: {self._title}, Author: {self._author}")
class DigitalLibraryBook(LibraryBook):
    def display_basic_info(self, file_format):
        super()._display_basic_info()
        print(f"File Format: {file_format}")
        book = LibraryBook("123456789", "Python Programming", "John Doe")
        print(book.get_ISBN())
        book.borrow_book("Alice")
        digital_book = DigitalLibraryBook("987654321","Digital Python", "Jane Doe")
        digital_book.display_basic_info("PDF")