import json
import logging

import azure.cosmos.exceptions as exceptions
import azure.functions as func

from service import category_service, book_service


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        category_data = list(category_service.get_category_basic_data_by_category_num())
        if len(category_data) == 0:
            return func.HttpResponse(status_code=404)

        return_value = []
        for value in category_data:
            value['book_count'] = book_service.get_books_count_by_category_num(value['category_num'])
            return_value.append(value)

        return func.HttpResponse(body=json.dumps(return_value), status_code=200, mimetype="application/json")
    except (exceptions.CosmosResourceExistsError, exceptions.CosmosHttpResponseError) as error:
        return func.HttpResponse(status_code=500, body=str({"error": error.message}), mimetype="application/json")
