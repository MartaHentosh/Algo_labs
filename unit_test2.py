import unittest

from lab2 import min_speed


class TestMinEatingSpeed(unittest.TestCase):
    def test_one(self):
        piles = [3, 6, 7, 11]
        H = 8
        self.assertEqual(min_speed(piles, H), 4)

    def test_two(self):
        piles = [30, 11, 23, 4, 20]
        H = 5
        self.assertEqual(min_speed(piles, H), 30)

    def test_three(self):
        piles = [30, 11, 23, 4, 20]
        H = 6
        self.assertEqual(min_speed(piles, H), 23)


if __name__ == '__main__':
    unittest.main()
