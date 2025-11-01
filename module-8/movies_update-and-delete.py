# D'Jon Harrison
# Date: 11.01.2025
# Assignment: Movies Table Queries with Insert, Update, Delete
# Purpose: Query MySQL movies database and display records in Python
# Sources:
# - MySQL Explained - Lesson 9
# - Sams Teach Yourself SQL in 10 Minutes - Lessons 10, 18, 19, Appendix B

import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="movies_user",
    password="popcorn",  # MySQL password
    database="movies"
)

cursor = db.cursor()

# Function to display films using INNER JOIN and order by film_id
def show_films(cursor, title):
    query = """
    SELECT film_name AS Name, film_director AS Director,
           genre_name AS Genre, studio_name AS 'Studio Name'
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    ORDER BY film_id;
    """
    cursor.execute(query)
    films = cursor.fetchall()
    print(f"\n-- {title} --")
    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name ID: {film[2]}\nStudio Name: {film[3]}\n")

# ---------------- DISPLAY ORIGINAL FILMS ----------------
show_films(cursor, "DISPLAYING FILMS")

# ---------------- INSERT NEW FILM ----------------
# Insert Star Wars (only if not already in table)
new_film_name = "Star Wars"
cursor.execute("SELECT COUNT(*) FROM film WHERE film_name = %s", (new_film_name,))
if cursor.fetchone()[0] == 0:
    insert_query = """
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    film_data = (new_film_name, "1977-05-25", 121, "George Lucas", 2, 2)
    cursor.execute(insert_query, film_data)
    db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# ---------------- UPDATE FILM ----------------
# Update Alien to Horror
update_query = "UPDATE film SET genre_id = 3 WHERE film_name = 'Alien';"
cursor.execute(update_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

# ---------------- DELETE FILM ----------------
# Delete Gladiator
delete_query = "DELETE FROM film WHERE film_name = 'Gladiator';"
cursor.execute(delete_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Close connection
cursor.close()
db.close()
