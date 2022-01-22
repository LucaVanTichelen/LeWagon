# pylint: disable=C0103, missing-docstring

def detailed_movies(db):
    '''return the list of movies with their genres and director name'''
    query = '''SELECT movies.title, movies.genres, directors.name
    FROM movies
    JOIN directors ON movies.director_id  = directors.id'''
    movies = db.execute(query).fetchall()
    return movies

def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    query = '''SELECT movies.title
    FROM movies
    JOIN directors ON movies.director_id = directors.id
    WHERE movies.start_year > directors.death_year'''
    movies = db.execute(query).fetchall()
    return [movie[0] for movie in movies]


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    query = f'''SELECT COUNT(movies.id), AVG(movies.minutes)
    FROM movies
    WHERE movies.genres LIKE "{genre_name}"'''
    movies = db.execute(query).fetchall()
    genre = {"genre": genre_name}
    genre["number_of_movies"] = movies[0][0]
    genre["avg_length"] = round(movies[0][1], 2)
    return genre

def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    query = f'''SELECT directors.name, COUNT(movies.genres)
    FROM movies JOIN directors
    ON movies.director_id  = directors.id
    WHERE movies.genres LIKE "{genre_name}"
    GROUP BY directors.name
    ORDER BY COUNT(movies.genres) DESC, directors.name LIMIT 5'''
    movies = db.execute(query).fetchall()
    return movies

def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    pass  # YOUR CODE HERE


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    query = f'''SELECT directors.name, movies.start_year - directors.birth_year
    FROM movies
    JOIN directors ON movies.director_id  = directors.id
    WHERE directors.birth_year > 0
    ORDER BY movies.start_year - directors.birth_year
    LIMIT 5'''
    movies = db.execute(query).fetchall()
    return movies


import sqlite3
conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
print(top_five_directors_for(db, "drama"))
