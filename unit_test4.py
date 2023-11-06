import unittest
from lab4 import find_minimum_depth


class TestGraphFunctions(unittest.TestCase):
    def test_find_minimum_depth(self):
        graph = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [8],
            8: [12],
            5: [9],
            6: [],
            7: [10, 11],
            9: [],
            10: [],
            11: []
        }

        self.assertEqual(find_minimum_depth(graph, 1), 3)
        self.assertEqual(find_minimum_depth(graph, 8), 2)


if __name__ == '__main__':
    unittest.main()
