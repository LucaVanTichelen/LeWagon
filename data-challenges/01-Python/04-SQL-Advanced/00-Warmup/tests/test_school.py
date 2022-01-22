# pylint: disable-all
import unittest
from school import students_from_city
import sqlite3

conn = sqlite3.connect('data/school.sqlite')
db = conn.cursor()


class TestSchool(unittest.TestCase):
    def test_paris(self):
        results = students_from_city(db, 'Paris')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 5)

    def test_london(self):
        results = students_from_city(db, 'London')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)

    def test_berlin(self):
        results = students_from_city(db, 'Berlin')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)

    def test_brussels(self):
        results = students_from_city(db, 'Brussels')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 1)

    def test_barcelona(self):
        results = students_from_city(db, 'Barcelona')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 0)
