# pylint: disable-all
import unittest
from queries import top_five_youngest_newly_directors
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

class TestTopFiveYoungestNewlyDirectors(unittest.TestCase):
    def test_is_list(self):
        results = top_five_youngest_newly_directors(db)
        expected = []
        self.assertEqual(type(results), type(expected))

    def test_length_list(self):
        results = top_five_youngest_newly_directors(db)
        self.assertEqual(len(results), 5)

    def test_first_element(self):
        results = top_five_youngest_newly_directors(db)
        expected = [
            ("Adam Paloian", 8),
            ("Alfonso Ribeiro", 19),
            ("Kenn Navarro", 20),
            ("Xavier Dolan", 20),
            ("Albert Hughes", 21)
        ]
        self.assertEqual(results, expected)
