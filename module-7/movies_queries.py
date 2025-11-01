# D'Jon Harrison
# Date: 10.22.2025
# Assignment: Movies Table Queries
# Purpose: Query MySQL movies database and display records in Python

import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="movies_user",
    password="popcorn",  # MySQL password
    database="movies"
)

cursor = db.cursor()

# Query 1: Display all records from the studio table
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
print("-- DISPLAYING Studio RECORDS --")
for studio in studios:
    print("Studio ID:", studio[0])
    print("Studio Name:", studio[1])
    print()  # blank line between records

# Query 2: Display all records from the genre table
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
print("-- DISPLAYING Genre RECORDS --")
for genre in genres:
    print("Genre ID:", genre[0])
    print("Genre Name:", genre[1])
    print()  # blank line between records

# Query 3: Display movies with runtime less than 120 minutes
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
short_films = cursor.fetchall()
print("-- DISPLAYING Short Film RECORDS --")
for film in short_films:
    print("Film Name:", film[0])
    print("Runtime:", film[1])
    print()  # blank line between records

# Query 4: Display film names and directors grouped by director
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
films_by_director = cursor.fetchall()
print("-- DISPLAYING Director RECORDS in Order --")
for film in films_by_director:
    print("Film Name:", film[0])
    print("Director:", film[1])
    print()  # blank line between records

# Close the database connection
cursor.close()
db.close()