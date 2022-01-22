from nbresult import ChallengeResultTestCase
import numpy as np


class TestStandardizer(ChallengeResultTestCase):
    def test_solution(self):
        truth_train = np.array([[-1.22474487, -1.22474487, -1.22474487],
                                [0., 0., 0.],
                                [1.22474487, 1.22474487, 1.22474487]])
        truth_test = np.array([[-1.22474487, -1.22474487, -1.22474487],
                               [0., 0., 0.],
                               [1.22474487, 1.22474487, 7.348469]])
        self.assertTrue(np.allclose(self.result.X_train_transformed, truth_train))
        self.assertTrue(np.allclose(self.result.X_test_transformed, truth_test))
