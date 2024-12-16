
import unittest
from books_service import BooksService

class TestBooksService(unittest.TestCase):

    def setUp(self):
            self.service = BooksService()

    def test_create_book(self):
        isbn = self.service.create("Python Grundlagen", price=25.99, pages=300, available=True)
        self.assertEqual(isbn, 1)
        book = self.service.find_by(isbn)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Python Grundlagen")
        self.assertTrue(book.available)

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as context:
            self.service.create("Ungültiges Buch", price=-10.0, pages=100)
        self.assertEqual(str(context.exception), "Invalid price, must be gte 0, was -10.0")

    def test_invalid_pages(self):
        with self.assertRaises(ValueError) as context:
            self.service.create("Ungültiges Buch", price=10.0, pages=0)
        self.assertEqual(str(context.exception), "Invalid pages, must be gt 0, was 0")

    def test_find_book_by_isbn(self):
        isbn = self.service.create("Python Grundlagen", price=25.99, pages=300)
        book = self.service.find_by(isbn)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Python Grundlagen")
        self.assertIsNone(self.service.find_by(99))

    def test_delete_book(self):
        isbn = self.service.create("Python Grundlagen", price=25.99, pages=300)
        self.assertTrue(self.service.delete_by(isbn))
        self.assertFalse(self.service.delete_by(isbn))
        self.assertIsNone(self.service.find_by(isbn))

    def test_find_all_books(self):
        self.service.create("Buch A", price=10.0, pages=100)
        self.service.create("Buch B", price=20.0, pages=200)
        books = self.service.find_all()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, "Buch A")
        self.assertEqual(books[1].title, "Buch B")

if __name__ == "__main__":
    unittest.main()
