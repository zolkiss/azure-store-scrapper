import json
import logging

import azure.cosmos.exceptions as exceptions
import azure.functions as func

from service import book_service


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        book_id = req.route_params['id']
        books = list(book_service.get_books_by_id(book_id))
        if (len(books) == 0):
            return func.HttpResponse(status_code=404)

        return func.HttpResponse(body=json.dumps(books[0]), status_code=200, mimetype="application/json")
    except (exceptions.CosmosResourceExistsError, exceptions.CosmosHttpResponseError) as error:
        return func.HttpResponse(status_code=500, body=str({"error": error.message}), mimetype="application/json")
