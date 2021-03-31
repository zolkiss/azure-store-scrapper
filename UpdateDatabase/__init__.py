import logging
import json
import azure.functions as func
import azure.cosmos.exceptions as exceptions

from . import book_crawler as bc
from . import db_util as du


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        processed_data = bc.process_url("https://books.toscrape.com")

        print(f"Number of read categories: {len(processed_data)}")
        du.recreate_database_data(processed_data)

        return func.HttpResponse(body=str({"message":"Everything was fine"}), status_code=200, mimetype="application/json")
    except (exceptions.CosmosResourceExistsError, exceptions.CosmosHttpResponseError) as error:
        return func.HttpResponse(status_code=500, body=str({"error": error.message}), mimetype="application/json")