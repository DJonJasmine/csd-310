# D'Jon Harrison
# Date: 11.01.2025
# Assignment: Module 8 - Movies Update and Delete
# Purpose: Insert, update, and delete records in the movies database and display results

# Sources:
# Read Textbook: MySQL Explained - Chapter 9
# MySQL Keywords and Reserved Words
# Read Textbook: Sams Teach Yourself SQL in 10 Minutes - Lesson 12
# Read Textbook: Sams Teach Yourself SQL in 10 Minutes - Lesson 13
# Read Textbook: Sams Teach Yourself SQL in 10 Minutes - Lesson 16
# Read Textbook: Sams Teach Yourself SQL in 10 Minutes - Appendix B
# Read Textbook: Sams Teach Yourself SQL in 10 Minutes - Appendix D

import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="movies_user",
    password="popcorn",
    database="movies"
)

cursor = db.cursor()

# Function to display films
def show_films(cursor, title):
    print(title)
    print()
    query = """
    SELECT film_name, film_director, genre_name, studio_name
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    ORDER BY film_id
    """
    cursor.execute(query)
    films = cursor.fetchall()
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre Name ID: {film[2]}")
        print(f"Studio Name: {film[3]}")
        print()  # Blank line between films

# DISPLAY FILMS BEFORE INSERT
show_films(cursor, "-- DISPLAYING FILMS --")

# INSERT a new film (Star Wars) using existing studio and genre IDs
insert_query = """
INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
VALUES (%s, %s, %s, %s, %s, %s)
"""
film_data = ("Star Wars", "1977-05-25", 121, "George Lucas", 2, 2)  # SciFi, 20th Century Fox
cursor.execute(insert_query, film_data)
db.commit()

# DISPLAY FILMS AFTER INSERT
show_films(cursor, "-- DISPLAYING FILMS AFTER INSERT --")

# UPDATE Alien's genre to Horror
update_query = """
UPDATE film
SET genre_id = 3
WHERE film_name = 'Alien'
"""
cursor.execute(update_query)
db.commit()

# DISPLAY FILMS AFTER UPDATE
show_films(cursor, "-- DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror --")

# DELETE Gladiator
delete_query = """
DELETE FROM film
WHERE film_name = 'Gladiator'
"""
cursor.execute(delete_query)
db.commit()

# DISPLAY FILMS AFTER DELETE
show_films(cursor, "-- DISPLAYING FILMS AFTER DELETE --")

# Close connection
cursor.close()
db.close()
