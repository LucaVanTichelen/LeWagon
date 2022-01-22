# pylint: disable-all
import unittest
from queries import detailed_orders
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()


class TestDetailOrders(unittest.TestCase):
    def test_length_results(self):
        results = detailed_orders(db)
        self.assertEqual(len(results), 20)

    def test_type_results(self):
        results = detailed_orders(db)
        self.assertIsInstance(results, list)

    def test_last_results(self):
        results = detailed_orders(db)
        expected = (20, 'Jim Wood', 'James')
        self.assertEqual(results[len(results) - 1], expected)

    def test_first_results(self):
        results = detailed_orders(db)
        expected = (1, 'Dick Terrcotta', 'James')
        self.assertEqual(results[0], expected)
