# pylint: disable-all
import unittest
from queries import best_employee
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()


class TestBestEmployee(unittest.TestCase):
    def test_length_results(self):
        results = best_employee(db)
        self.assertEqual(len(results), 3)

    def test_first_name_in_results(self):
        results = best_employee(db)
        self.assertTrue('Patty' in results)

    def test_last_name_in_results(self):
        results = best_employee(db)
        self.assertTrue('Lee' in results)

    def test_amount_in_results(self):
        results = best_employee(db)
        self.assertTrue(7945.6 in results)

    def test_type_result(self):
        results = best_employee(db)
        self.assertIsInstance(results, tuple)
