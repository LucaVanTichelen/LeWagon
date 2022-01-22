# pylint: disable-all
import unittest
from queries import average_number_of_days_between_orders
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()

class TestAverageNumberOfDaysBetweenOrders(unittest.TestCase):
    def test_result_type(self):
        result = average_number_of_days_between_orders(db)
        self.assertIsInstance(result, int)

    def test_result_value(self):
        result = average_number_of_days_between_orders(db)
        expected = 89
        self.assertEqual(result, expected)
