import unittest

from lab1 import find_largest_number


class TestFindLargestNumber(unittest.TestCase):
    def test_first(self):
        nums = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 2
        result = find_largest_number(nums, k)
        self.assertEqual(result, (36, 1))

    def test_second(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 3
        result = find_largest_number(nums, k)
        self.assertEqual(result, (4, 2))

    def test_third(self):
        nums = [7, 8, 9, 10, 11, 12]
        k = 4
        result = find_largest_number(nums, k)
        self.assertEqual(result, (9, 3))
