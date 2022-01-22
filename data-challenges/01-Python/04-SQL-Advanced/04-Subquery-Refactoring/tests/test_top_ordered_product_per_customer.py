# pylint: disable-all
import unittest
from queries import top_ordered_product_per_customer
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()

class TestTopOrderedProductPerCustomer(unittest.TestCase):
    expected = [
        (4, 6, 5876),
        (2, 5, 2791.6),
        (1, 6, 1909.7),
        (3, 3, 1200),
        (5, 6, 1175.2)
    ]

    def test_result_type(self):
        results = top_ordered_product_per_customer(db)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], tuple)

    def test_result_length(self):
        results = top_ordered_product_per_customer(db)
        self.assertEqual(len(results), len(TestTopOrderedProductPerCustomer.expected))

    def test_result_values(self):
        results = top_ordered_product_per_customer(db)
        self.assertEqual(results[0], TestTopOrderedProductPerCustomer.expected[0])
        self.assertEqual(results[-1], TestTopOrderedProductPerCustomer.expected[-1])


