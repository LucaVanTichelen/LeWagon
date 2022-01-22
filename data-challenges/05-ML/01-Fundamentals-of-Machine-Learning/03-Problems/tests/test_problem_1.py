from nbresult import ChallengeResultTestCase


class TestProblem_1(ChallengeResultTestCase):
    def test_problem_1(self):
        self.assertGreater(self.result.answer, 1000)
        self.assertLess(self.result.answer, 2500)
