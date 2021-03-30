import json


class category():
    def __init__(self, id: int, technical_name: str, readable_name: str):
        self.id = id
        self.technical_name = technical_name
        self.readable_name = readable_name


class book():
    def __init__(self,  id: int, technical_name: str, category: category, title: str, description: str = "", upc: str = None, currency: str = None, net_price: float = None, gross_price: float = None, tax: float = None, availability: int = None, number_of_reviews: int = None):
        self.id = id
        self.technical_name = technical_name
        self.category = category
        self.title = title
        self.description = description
        self.upc = upc
        self.currency = currency
        self.net_price = net_price
        self.gross_price = gross_price,
        self.tax = tax,
        self.availability = availability
        self.number_of_reviews = number_of_reviews

    def as_dict(self):
        temp_dict = {"id": self.id, "technical_name": self.technical_name, "title": self.title, "category": self.category.__dict__}
        if (self.upc != None):
            temp_dict["description"] = self.description
            temp_dict["upc"] = self.upc
            temp_dict["currency"] = self.currency
            temp_dict["net_price"] = self.net_price
            temp_dict["gross_price"] = self.gross_price
            temp_dict["tax"] = self.tax
            temp_dict["availability"] = self.availability
            temp_dict["number_of_reviews"] = self.number_of_reviews
        return temp_dict
