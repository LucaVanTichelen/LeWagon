from nbresult import ChallengeResultTestCase
import numpy as np


class TestBlobs(ChallengeResultTestCase):
    def test_shape(self):
        self.assertEqual(self.result.shape, (500, 2))

    def test_lower_centroid(self):
        self.assertTrue(np.all(self.result.lower_centroid < 0))
