Library API
This is a library API developed using Django and integrated with Docker and PostgreSQL. The API allows users to interact with a library database, including adding, updating, and deleting books, as well as searching for books by title, author, or ISBN.

Getting Started
To get started with the API, you will need to have Docker and Docker Compose installed on your machine. Once you have those set up, you can clone the repository and run the following command in the root directory:

Copy code
docker-compose up
This will start the API and PostgreSQL in separate containers. The API will be available at http://localhost:8000/ and the PostgreSQL database will be available at postgres://postgres:postgres@localhost:5432/library.

Usage
The API has several endpoints that allow you to interact with the library database.

/books/ - Retrieve a list of all books in the library.
/books/<int:pk>/ - Retrieve a specific book by its primary key.
/authors/ -Retrieve a list of all authors in the library.
/authors/int:pk>/ - Create a new authors in the library.

