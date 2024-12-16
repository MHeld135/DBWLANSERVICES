
from book import Book

class BooksService:
    def __init__(self):
        self.books = {}  # Speicherung in einem Dictionary#
        self.next_isbn = 1  # Auto-ISBN-Nummer#

    def create(self, title: str, price: float = 0.0, pages: int = 1, available: bool = False) -> int:
        if price < 0:
            raise ValueError(f"Invalid price, must be gte 0, was {price}")
        if pages <= 0:
            raise ValueError(f"Invalid pages, must be gt 0, was {pages}")

        book = Book(isbn=self.next_isbn, title=title, price=price, pages=pages, available=available)
        self.books[self.next_isbn] = book
        self.next_isbn += 1
        return book.isbn

    def find_by(self, isbn: int) -> Book | None:
        return self.books.get(isbn)

    def find_all(self) -> list[Book]:
        return list(self.books.values())

    def delete_by(self, isbn: int) -> bool:
        if isbn in self.books:
            del self.books[isbn]
            return True
        return False
