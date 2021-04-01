import json
import logging

import azure.cosmos.exceptions as exceptions
import azure.functions as func

from service import category_service


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        books = list(category_service.get_categories())
        return func.HttpResponse(body=json.dumps(books), status_code=200, mimetype="application/json")
    except (exceptions.CosmosResourceExistsError, exceptions.CosmosHttpResponseError) as error:
        return func.HttpResponse(status_code=500, body=str({"error": error.message}), mimetype="application/json")
