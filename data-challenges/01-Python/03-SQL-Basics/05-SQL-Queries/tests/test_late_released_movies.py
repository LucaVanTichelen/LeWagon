# pylint: disable-all
import unittest
from queries import late_released_movies
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

class TestLateReleasedMovies(unittest.TestCase):
    def test_is_list(self):
        results = late_released_movies(db)
        expected = []
        self.assertEqual(type(results), type(expected))

    def test_length_list(self):
        results = late_released_movies(db)
        self.assertEqual(len(results), 6)

    def test_first_element(self):
        results = late_released_movies(db)
        expected = [
            "Cars",
            "Fantasia 2000",
            "Game of Death",
            "The Many Adventures of Winnie the Pooh",
            "The Rescuers",
            "Waitress"
        ]
        self.assertEqual(set(results), set(expected))



