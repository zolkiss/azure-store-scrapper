Azure Store Scrapper
====================

State
-----

Project init

Endpoints
---------

- [SERVER_URL]/api/book - Returns all the books
- [SERVER_URL]/api/book/{id} - Returns the given book by ID
- [SERVER_URL]/api/book/complex/mostExpensive - Returns the most expensive books with the price
- [SERVER_URL]/api/book/complex/countByCategory - Returns the number of the books in the category
- [SERVER_URL]/api/book/category/{category_num} - Returns all the books by category number (not the ID)
- [SERVER_URL]/api/category - Returns all the category
- [SERVER_URL]/api/category/{id} - Returns the category by ID
- [SERVER_URL]/api/category/num/{category_num} - Returns the category by the category_num field
- [SERVER_URL]/api/UpdateDatabase - Returns not, but removes the data from database, and re-scrap the page

Server setup
------------

- Azure Cosmos DB as backend
    - The configuration parameters are held in env variables
    - The DB is only reachable from the AZ network
- Every end-point is a different Azure Function file
    - For every endpoint you need "admin" authentication level