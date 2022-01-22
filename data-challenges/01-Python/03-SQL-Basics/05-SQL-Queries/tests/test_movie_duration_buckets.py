# pylint: disable-all
import unittest
from queries import movie_duration_buckets
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

class TestMovieDurationBuckets(unittest.TestCase):
    def test_movie_duration_buckets(self):
        res = movie_duration_buckets(db)
        solution = [
            (30, 292),
            (60, 764),
            (90, 1362),
            (120, 5302),
            (150, 1617),
            (180, 331),
            (210, 88),
            (240, 19),
            (270, 7),
            (300, 11),
            (330, 4),
            (360, 7),
            (390, 7),
            (420, 4),
            (450, 4),
            (480, 2),
            (540, 4),
            (570, 3),
            (600, 4),
            (630, 2),
            (690, 2),
            (900, 1),
            (1020, 1)
        ]
        self.assertIs(type(solution), list)
        self.assertIs(type(solution[0]), tuple)
        self.assertEqual(res, solution)
