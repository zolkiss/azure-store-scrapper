from util import db_util


def get_categories():
    container_client = db_util.create_database_container_client()
    return container_client.query_items(query="SELECT * FROM c WHERE c._type='Category'",
                                        enable_cross_partition_query=True)


def get_categories_by_id(category_id):
    container_client = db_util.create_database_container_client()
    return container_client.query_items(query="SELECT * FROM c WHERE c._type='Category' AND c.id=@categoryId",
                                        enable_cross_partition_query=True, parameters=[
            {"name": "@categoryId", "value": category_id}
        ])


def get_categories_by_category_num(category_num):
    container_client = db_util.create_database_container_client()
    return container_client.query_items(
        query="SELECT * FROM c WHERE c._type='Category' AND c.category_num=@categoryNum",
        parameters=[
            {"name": "@categoryNum", "value": category_num}
        ])
