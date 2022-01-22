from nbresult import ChallengeResultTestCase


class TestImageShape(ChallengeResultTestCase):
    def test_img_shape(self):
        self.assertEqual(self.result.img_shape, (512, 512, 3))
