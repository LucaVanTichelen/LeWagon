from nbresult import ChallengeResultTestCase


class TestClassification(ChallengeResultTestCase):
    def test_best_pc_number(self):
        self.assertGreater(self.result.best_pc, 200)
        self.assertLess(self.result.best_pc, 600)
