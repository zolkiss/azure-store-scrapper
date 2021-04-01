import json
import logging

import azure.cosmos.exceptions as exceptions
import azure.functions as func

from service import book_service


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        max_price = 0.0
        list_of_books = []
        for book in book_service.get_books():
            if book['net_price'] > max_price:
                max_price = book['net_price']
                list_of_books = [book]
            elif book['net_price'] == max_price:
                list_of_books.append(book)

        return func.HttpResponse(body=json.dumps(list_of_books), status_code=200, mimetype="application/json")
    except (exceptions.CosmosResourceExistsError, exceptions.CosmosHttpResponseError) as error:
        return func.HttpResponse(status_code=500, body=str({"error": error.message}), mimetype="application/json")
