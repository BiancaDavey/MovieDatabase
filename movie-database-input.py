#!/usr/bin/env python3

# This application for the client MovieDirect provides a function enabling the user to insert a new record into the Movies database.

import psycopg2
import re #  Imported to enable pattern-matching for user input validation.

def main():

    print("Welcome to MovieDirect!")

    """- Movies table. Here to show column list
    CREATE TABLE Movies (
    movie_id integer NOT NULL,
    movie_title character varying(100) NOT NULL,
    director_last_name character varying(50) NOT NULL,
    director_first_name character varying(50) NOT NULL,
    genre character varying(20) CHECK genre IN 'Action', 'Adventure', 'Comedy', Romance', 'Science Fiction', 'Documentary', 'Drama', 'Horror',
    media_type character varying(20) CHECK media_type IN 'Blu-ray', 'DVD',
    release_date date,
    studio_name character varying(50),
    retail_price real CHECK retail price > 0,
    current_stock integer CHECK current_stock >= 0
    );
    """

    # User input is taken for the database, username and password and used to connect to the database.

    database_name = input("database: ")
    username = input("username: ")
    user_password = input("password: ")

    # genres represents the CHECK constraint placed on the values of genre in the movies database.

    genres = ("Action", "Adventure", "Comedy", "Romance", "Science Fiction", "Documentary", "Drama", "Horror")

    # mediaTypes represents the CHECK constraint placed on the values of media_type in the movies database.

    mediaTypes = ("Blu-ray", "DVD")

    # While loops are used to take user input for each field of data to be inserted as a part of the new record.
    # Try and except statements are used within each while loop to validate each field of user input.
    #
    # User input for each field is validated for compliance with data types and check constraints set for each value in the database.
    # The input of NULL values is precluded by the validation for each field, ensuring that no NULL constraints are violated.
    #
    # Non-complying input is re-prompted after entry before the program moves to the next field of input.
    # This approach enables evaluation of the input data before the SQL insertion containing it is executed.

    #  While loop ensures that the user inputs an integer value.

    while True:
        try:
            movieId = int(input("Please enter the id for the new movie: "))
            break
        except (ValueError):
            print("Please enter an integer for the movie id.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    #  While loop ensures that the user enters a value between 1-100 characters, and does not input only blank space.

    while True:
        try:
            movieTitle = input("Please enter the title for the new movie: ")
            if len(movieTitle) == 0 or len(movieTitle) > 100 or len(movieTitle) == movieTitle.count(" "):
                raise(ValueError)
            break
        except (ValueError):
            print("Movie title must be between 1 and 100 characters long and not consist only of blank spaces.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    #  While loop ensures that the user enters a value between 1-100 characters, and does not input only blank space.

    while True:
        try:
            directorFirstName = input("Please enter the director's first name: ")
            if len(directorFirstName) == 0 or len(directorFirstName) > 50 or len(directorFirstName) == directorFirstName.count(" "):
                raise(ValueError)
            break
        except (ValueError):
            print("Director's first name must be between 1 and 50 characters long and not consist only of blank spaces.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    #  While loop ensures that the user enters a value between 1-50 characters, and does not input only blank space.

    while True:
        try:
            directorLastName = input("Please enter the director's last name: ")
            if len(directorLastName) == 0 or len(directorLastName) > 50 or len(directorLastName) == directorLastName.count(" "):
                raise(ValueError)
            break
        except (ValueError):
            print("Director's last name must be between 1 and 50 characters long and not consist only of blank spaces.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    #  While loop ensures that the user enters a value matching a genre value set by the CHECK constraint in the database.

    while True:
        try:
            genre = input("Please enter the genre of the new movie: ")
            if genre not in genres:
                raise(ValueError)
            break
        except (ValueError):
            print("Please select a genre from Action, Adventure, Comedy, Romance, Science Fiction, Documentary, Drama, or Horror.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    #  While loop ensures that the user enters a value matching a media_type value set by the CHECK constraint in the database.

    while True:
        try:
            mediaType = input("Please enter the media type: ")
            if mediaType not in mediaTypes:
                raise(ValueError)
            break
        except (ValueError):
            print("Please select a media type from DVD or Blu-ray.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    #  While loop ensures that the user enters a release date in the YYYY-MM-DD format used in the database.

    while True:
        try:
            releaseDate = input("Please enter the release date: ")
            if not re.match(r"\d{4}[-/]\d{2}[-/]\d{2}", releaseDate):
                raise(ValueError)
            break
        except (ValueError):
            print("Please use YYYY-MM-DD format for the date.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    #  While loop ensures that the user enters a value between 1-50 characters, and does not input only blank space.

    while True:
        try:
            studioName = input("Please enter the movie's studio: ")
            if len(studioName) == 0 or len(studioName) > 50 or len(studioName) == studioName.count(" "):
                raise(ValueError)
            break
        except (ValueError):
            print("Studio name must be between 1 and 50 characters long and not consist only of blank spaces.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    #  While loop ensures that the user enters a positive integer that can be converted from a float type to the real data type specified in the database.

    while True:
        try:
            retailPrice = float(input("Please enter the retail price of the movie: "))
            if retailPrice <= 0:
                raise(ValueError)
            break
        except (ValueError):
            print("Please enter a non-negative number for retail price.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    #  While loop ensures that the user inputs a non-negative integer value.

    while True:
        try:
            currentStock = int(input("Please enter the number of copies in stock: "))
            if currentStock <= 0:
                raise(ValueError)
            break
        except (ValueError):
            print("Please enter a positive integer for current stock.")
        except (IOError):
            print("Error reading the file.")
        except (Error):
            print("An error occurred. Please re-enter the information.")

    # SQL query template specifying the attributes into which the new values will be inserted.

    sql = """INSERT INTO Movies(movie_id, movie_title, director_first_name, director_last_name, genre, media_type, release_date, studio_name, retail_price, current_stock) VALUES%s;"""

    # Takes the user's input as the row list to insert into the database.

    insert_movie_list = (movieId, movieTitle, directorFirstName, directorLastName, genre, mediaType, releaseDate, studioName, retailPrice, currentStock)

    # Connects to the database.

    conn = None
    try:

       # Connects to database using the input prompted from the user.

        conn = psycopg2.connect(dbname=database_name,
                               user =username,
                               host='127.0.0.1',
                               password=user_password)

       # Creates database cursor.

        cur = conn.cursor()

       # Executes the SQL insert statement, allowing execute to sanitize.

        cur.execute(sql,(insert_movie_list,))

       # Commits changes to the database.

        conn.commit()

        print("Success! A new entry for Movies has been entered into the database.")

    # Error handling for failing to connect to the database.

    except (Exception, psycopg2.IntegrityError) as integrityError:
        print("Integrity error:", integrityError)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error connecting to database: ", error)

    # Closes the database at the end of the transaction.

    finally:
        if(conn):
            cur.close()
            conn.close()
            print("Connection closed")

# Function call for the program to run.

if __name__ == "__main__":
    main()
