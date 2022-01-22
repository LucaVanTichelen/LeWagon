# pylint: disable-all
import unittest
from queries import query_orders
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()


class TestQueryOrders(unittest.TestCase):
    def test_length_list(self):
        results = query_orders(db)
        self.assertEqual(len(results), 20)

    def test_first_element(self):
        results = query_orders(db)
        result_0 = results[0]
        expected = (1, 1, 1, '2012-01-04', '2012-01-09', '2012-01-05', 1, 3.75)
        self.assertEqual(result_0, expected)
