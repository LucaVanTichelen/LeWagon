# pylint: disable-all
import unittest
from queries import best_customers
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()

class TestBestCustomers(unittest.TestCase):
    def test_type_results(self):
        results = best_customers(db)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], tuple)

    def test_length_results(self):
        results = best_customers(db)
        self.assertEqual(len(results), 3)

    def test_results(self):
        results = best_customers(db)
        expected = [(4, 2175.03), (5, 1096.3), (2, 1031.24)]
        self.assertEqual(results, expected)

