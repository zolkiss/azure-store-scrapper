import logging
import json
import azure.functions as func

from . import book_crawler as bc
from .classes import book


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    processed_data = bc.process_url("https://books.toscrape.com")

    return func.HttpResponse(body = str(list(map(lambda book: serialize(book), processed_data))), status_code=200, mimetype="application/json")

def serialize(book: book):
    return book.as_dict()