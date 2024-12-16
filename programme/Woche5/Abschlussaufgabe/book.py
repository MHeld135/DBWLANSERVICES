
class Book:
    def __init__(self, isbn: int, title: str, price: float, pages: int, available: bool):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.pages = pages
        self.available = available

    def __eq__(self, other):
        #Vergleich der Bücher durch ISBN#
        return isinstance(other, Book) and self.isbn == other.isbn

    def __str__(self):
            return (f"ISBN: {self.isbn}, Titel: {self.title}, Preis: {self.price:.2f} EUR, "
                f"Seiten: {self.pages}, Verfügbar: {'Ja' if self.available else 'Nein'}")
