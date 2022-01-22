# pylint: disable-all
import unittest
from queries import get_orders_range
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()


class TestOrdersRange(unittest.TestCase):
    def test_type_results(self):
        date_from = "2012-01-04"
        date_to = "2012-03-04"
        results = get_orders_range(db, date_from, date_to)
        self.assertIsInstance(results, list)

    def test_len_results(self):
        date_from = "2012-01-04"
        date_to = "2012-03-04"
        results = get_orders_range(db, date_from, date_to)
        self.assertEqual(len(results), 2)

    def test_results_0(self):
        date_from = "2012-01-04"
        date_to = "2012-03-04"
        results = get_orders_range(db, date_from, date_to)
        expected = [
            (2, 2, 2, '2012-01-27', '2012-02-01', '2012-01-28', 1, 7.25),
            (3, 4, 1, '2012-02-19', '2012-02-24', '2012-02-23', 2, 5.5)
        ]
        self.assertEqual(results, expected)

    def test_results_1(self):
        date_from = "2012-03-15"
        date_to = "2012-04-15"
        results = get_orders_range(db, date_from, date_to)
        expected = [
            (5, 4, 2, '2012-04-05', '2012-04-10', '2012-04-06', 3, 8.75)
        ]
        self.assertEqual(results, expected)
