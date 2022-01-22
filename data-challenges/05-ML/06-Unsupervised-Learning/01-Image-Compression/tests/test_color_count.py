from nbresult import ChallengeResultTestCase


class TestColorCount(ChallengeResultTestCase):
    def test_color_count(self):
        self.assertEqual(self.result.color_count, 113382)
