# pylint: disable-all
import unittest
from queries import orders_per_customer
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()


class TestOrdersPerCustomer(unittest.TestCase):
    def test_length_results(self):
        results = orders_per_customer(db)
        self.assertEqual(len(results), 6)

    def test_first_result(self):
        results = orders_per_customer(db)
        expected = ('Sebastien Saunier', 0)
        self.assertEqual(results[0], expected)

    def test_last_result(self):
        results = orders_per_customer(db)
        expected = ('Jim Wood', 6)
        self.assertEqual(results[-1], expected)

    def test_type_result(self):
        results = orders_per_customer(db)
        self.assertIsInstance(results, list)
