# pylint: disable-all
import unittest
from queries import get_average_purchase
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()

class TestAveragePerCustomer(unittest.TestCase):
    def test_type_results(self):
        results = get_average_purchase(db)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], tuple)

    def test_length_results(self):
        results = get_average_purchase(db)
        self.assertEqual(len(results), 5)

    def test_results(self):
        results = get_average_purchase(db)
        expected = [(1, 673.9), (2, 1031.24), (3, 266.32), (4, 2175.03), (5, 1096.3)]
        self.assertEqual(results[0], expected[0])
        self.assertEqual(results[-1], expected[-1])

