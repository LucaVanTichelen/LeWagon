from nbresult import ChallengeResultTestCase


class TestProblem_2(ChallengeResultTestCase):
    def test_problem_2(self):
        self.assertGreater(self.result.answer, 0.9)
        self.assertLess(self.result.answer, 1)
