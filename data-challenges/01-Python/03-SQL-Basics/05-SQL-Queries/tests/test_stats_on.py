# pylint: disable-all
import unittest
from queries import stats_on
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()


class TestStatsOn(unittest.TestCase):
    def test_is_dict(self):
        results = stats_on(db, "Action,Adventure,Comedy")
        expected = {}
        self.assertEqual(type(results), type(expected))

    def test_results_for_action_adv(self):
        results = stats_on(db, "Action,Adventure,Comedy")
        expected = {
            'genre': 'Action,Adventure,Comedy',
            'number_of_movies': 153,
            'avg_length': 100.98
        }
        self.assertEqual(results, expected)

    def test_results_for_drama(self):
        results = stats_on(db, "Drama,Mystery")
        expected = {
            'genre': 'Drama,Mystery',
            'number_of_movies': 23,
            'avg_length': 98.65
        }
        self.assertEqual(results, expected)
