# pylint: disable-all
import unittest
from queries import detailed_movies
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

class TestDetailedMovies(unittest.TestCase):
    def test_is_list(self):
        results = detailed_movies(db)
        expected = []
        self.assertEqual(type(results), type(expected))

    def test_length_list(self):
        results = detailed_movies(db)
        self.assertEqual(len(results), 9872)

    def test_first_element(self):
        results = detailed_movies(db)
        result_0 = results[0]
        expected = (
            'A Trip to the Moon',
            'Action,Adventure,Comedy',
            'Georges Méliès'
        )
        self.assertEqual(result_0, expected)

    def test_len_each_tuple(self):
        results = detailed_movies(db)
        for r in results:
            self.assertEqual(len(r), 3)
