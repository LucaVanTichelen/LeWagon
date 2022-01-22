# pylint: disable=missing-docstring, C0103

# => list (rows) of tuples (columns)


def directors_count(db):
    # return the number of directors contained in the database
    query = "SELECT COUNT(imdb_director_id) FROM directors"
    db.execute(query)
    results = db.fetchall()
    return results[0][0]

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = "SELECT name FROM directors"
    db.execute(query)
    results = db.fetchall()
    directors = []
    for result in results:
        directors.append(result[0])
    return sorted(directors)

def love_movies(db):
    # return the list of all movies which contain the word "love" in their
    # title, sorted in alphabetical order
    query = "SELECT * FROM movies WHERE(movies.title) LIKE '%love%'"
    db.execute(query)
    results = db.fetchall()
    movies = []
    for movie in results:
        movies.append(movie[0])
    return sorted(movies)

def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = f"SELECT count(*) FROM directors WHERE(directors.name) LIKE '%{name}%'"
    db.execute(query)
    count = db.fetchall()
    return count[0][0]

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f"SELECT * FROM movies WHERE movies.minutes > {min_length}"
    db.execute(query)
    results = db.fetchall()
    movies = []
    for movie in results:
        movies.append(movie[0])
    return sorted(movies)
