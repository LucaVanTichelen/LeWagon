# pylint: disable-all
import unittest
from queries import top_five_directors_for
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()


class TestTopFiveDirectorsFor(unittest.TestCase):
    def test_return_list(self):
        results = top_five_directors_for(db, "Action,Adventure,Comedy")
        expected = []
        self.assertEqual(type(results), type(expected))

    def test_return_right_results1(self):
        results = top_five_directors_for(db, "Action,Adventure,Comedy")
        expected = [
            ('Robert Rodriguez', 5),
            ('Jonathan Frakes', 4),
            ('Anthony C. Ferrante', 3),
            ('Barry Sonnenfeld', 3),
            ('Jackie Chan', 3)
        ]
        self.assertEqual(results, expected)

    def test_return_5_results(self):
        results = top_five_directors_for(db, "Action,Adventure,Comedy")
        self.assertEqual(len(results), 5)

    def test_return_right_results2(self):
        results = top_five_directors_for(db, "Drama,Mystery")
        expected = [
            ('Aaron Schneider', 1),
            ('Alain Resnais', 1),
            ('Asghar Farhadi', 1),
            ('Bill Condon', 1),
            ('Chang-dong Lee', 1)
        ]
        self.assertEqual(results, expected)
