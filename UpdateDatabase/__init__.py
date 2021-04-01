import logging

import azure.cosmos.exceptions as exceptions
import azure.functions as func

from util import db_util as du
from . import book_crawler as bc


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        logging.info("Starting the scrapping!")
        processed_data = bc.process_url("https://books.toscrape.com")

        logging.info(f"The scrapping is finished! Number of read categories: {len(processed_data)}")
        logging.info("Starting to save the scrapped data")
        du.recreate_database_data(processed_data)

        return func.HttpResponse(body=str({"message": "Everything was fine"}), status_code=200,
                                 mimetype="application/json")
    except (exceptions.CosmosResourceExistsError, exceptions.CosmosHttpResponseError) as error:
        return func.HttpResponse(status_code=500, body=str({"error": error.message}), mimetype="application/json")