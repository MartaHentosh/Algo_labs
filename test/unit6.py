import unittest
import sys
import os

sys.path.append(os.path.abspath('C:/Users/marta/Algo/lab6/src'))

from function import find_last_occurrence


class TestNeedleSearch(unittest.TestCase):
    def test_find_last_occurrence_1(self):
        haystack = "abracadabra"
        needle = "abra"
        expected_result = (7, 24)
        result = find_last_occurrence(haystack, needle)
        self.assertEqual(result, expected_result)
        print(f"Test 1 Passed. Result: {result}")

    def test_find_last_occurrence_2(self):
        haystack = "hello world"
        needle = "world"
        expected_result = (6, 18)
        result = find_last_occurrence(haystack, needle)
        self.assertEqual(result, expected_result)
        print(f"Test 2 Passed. Result: {result}")


if __name__ == '__main__':
    unittest.main()
