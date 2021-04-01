import uuid


class Category:
    def __init__(self, category_num: str, technical_name: str, readable_name: str):
        self.id = str(uuid.uuid4())
        self.category_num = category_num
        self.technical_name = technical_name
        self.readable_name = readable_name
        self._type = "Category"


class Book:
    def __init__(self, technical_name: str, category_num: str, book_num: str, title: str, description: str = "",
                 upc: str = None, currency: str = None, net_price: float = None, gross_price: float = None,
                 tax: float = None, availability: int = None, number_of_reviews: int = None):
        self.id = str(uuid.uuid4())
        self.technical_name = technical_name
        self.category_num = category_num
        self.book_num = book_num
        self.title = title
        self.description = description
        self.upc = upc
        self.currency = currency
        self.net_price = net_price
        self.gross_price = gross_price,
        self.tax = tax,
        self.availability = availability
        self.number_of_reviews = number_of_reviews
        self._type = "Book"
