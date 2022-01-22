# pylint: disable-all
import unittest
from queries import spent_per_customer
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()


class TestSpentCustomer(unittest.TestCase):
    def test_type_results(self):
        results = spent_per_customer(db)
        self.assertIsInstance(results, list)

    def test_first_result(self):
        results = spent_per_customer(db)
        expected = ('Jim Wood', 1597.9)
        self.assertEqual(results[0], expected)

    def test_last_result(self):
        results = spent_per_customer(db)
        expected = ('Toni Faucet', 8700.1)
        self.assertEqual(results[len(results)-1], expected)

    def test_len_resultts(self):
        results = spent_per_customer(db)
        self.assertEqual(len(results), 5)
