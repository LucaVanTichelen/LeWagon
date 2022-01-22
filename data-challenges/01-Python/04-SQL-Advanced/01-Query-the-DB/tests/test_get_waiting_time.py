# pylint: disable-all
import unittest
from queries import get_waiting_time
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()


class TestWaitingTime(unittest.TestCase):
    def test_size_list(self):
        results = get_waiting_time(db)
        self.assertEqual(len(results), 20)

    def test_type_results(self):
        results = get_waiting_time(db)
        self.assertIsInstance(results, list)

    def test_first_result(self):
        results = get_waiting_time(db)
        expected = \
            (1, 1, 1, '2012-01-04', '2012-01-09', '2012-01-05', 1, 3.75, 1.0)
        self.assertEqual(results[0], expected)

    def test_last_result(self):
        results = get_waiting_time(db)
        expected = \
            (19, 2, 4, '2013-02-21', '2013-02-26', '2013-03-01', 4, 14.0, 8.0)
        self.assertEqual(results[len(results) - 1], expected)
