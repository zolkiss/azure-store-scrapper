import logging

import azure.cosmos.cosmos_client as cosmos_client

from UpdateDatabase.classes import Book
from UpdateDatabase.classes import Category
from util import cosmos_config

HOST = cosmos_config.settings['host']
MASTER_KEY = cosmos_config.settings['master_key']
DATABASE_ID = cosmos_config.settings['database_id']
CONTAINER_ID = cosmos_config.settings['container_id']


def create_database_container_client():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBDotnetQuickstart",
                                        user_agent_overwrite=True)
    db = client.get_database_client(DATABASE_ID)
    return db.get_container_client(CONTAINER_ID)


def recreate_database_data(category_with_books):
    container_client = create_database_container_client()

    logging.info("Clearing database")
    clear_database(container_client)

    for category_and_book in category_with_books:
        logging.info(f"Saving category: {category_and_book[0].technical_name}")
        save_category(category_and_book[0], container_client)
        for book in category_and_book[1]:
            logging.info(f"Saving book '{book.technical_name} to category '{category_and_book[0].technical_name}'")
            save_book(book, container_client)


def clear_database(container_client):
    documents = list(container_client.query_items(query="SELECT * FROM c", enable_cross_partition_query=True))
    for document in documents:
        container_client.delete_item(
            item=document['id'], partition_key=document['category_num'])


def save_category(category_data: Category, container_client):
    container_client.create_item(category_data.__dict__)


def save_book(book_data: Book, container_client):
    container_client.create_item(book_data.__dict__)
