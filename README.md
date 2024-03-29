# Movie Database

Movie Database is a program enabling users to create new entries for a PostgreSQL database containing movies, with data input being verified for compliance with database constraints before being sent to the database server.

## Features

* User input is validated according to the data contraints placed in the database
* Data is verified on the client side of the application
* Data sent to the PostgreSQL database is already pre-verified for compliance with database constraints
* Error handling for user input and server connectivity
* Clear user prompts and error messages
* User authentication with credential check before establishing server connection

## Installation

Python 3 is required to run this program.

psycopg2 is required to run this program.

SQL is required to run this program.

## Usage

1. Run the program using the command `python3 movie-database-input.py`.
2. Input values for each field of the data entry as prompted.
3. Once verified, a connection to the server is established and the data is sent to the database.

## Usage example

```
python3 movie-database-input.py
```

[![Movie-Database-Input-verification.png](https://i.postimg.cc/RFcXFJ5P/Movie-Database-Input-verification.png)](https://postimg.cc/tZ4hvTgP)

## Author

Bianca Davey

biancamdavey91@gmail.com
