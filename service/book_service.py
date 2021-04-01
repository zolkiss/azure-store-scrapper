from util import db_util


def get_books():
    container_client = db_util.create_database_container_client()
    return container_client.query_items(query="SELECT * FROM c WHERE c._type='Book'", enable_cross_partition_query=True)


def get_books_by_id(book_id):
    container_client = db_util.create_database_container_client()
    return container_client.query_items(query="SELECT * FROM c WHERE c._type='Book' AND c.id=@bookId",
                                        enable_cross_partition_query=True, parameters=[
            {"name": "@bookId", "value": book_id}
        ])


def get_books_by_category_num(category_num):
    container_client = db_util.create_database_container_client()
    return container_client.query_items(query="SELECT * FROM c WHERE c._type='Book' AND c.category_num=@categoryNum",
                                        parameters=[
                                            {"name": "@categoryNum", "value": category_num}
                                        ])
