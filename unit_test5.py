import unittest

from lab5.lab5_3 import count_cross_tribal_pairs, read_input, write_output


class TestCountCrossTribalPairs(unittest.TestCase):

    def test_count_cross_tribal_pairs(self):
        N = 5
        pairs = [(1, 2), (2, 4), (3, 5), (8, 10), (1, 3)]
        result = count_cross_tribal_pairs(N, pairs)
        self.assertEqual(result, 6)

    def test_read_input(self):
        # read_input
        input_data = "5\n1 2\n2 4\n3 5\n8 10\n1 3\n"
        with open('test_input', 'w') as test_input_file:
            test_input_file.write(input_data)
        N, pairs = read_input('test_input')
        self.assertEqual(N, 5)
        self.assertEqual(pairs, [(1, 2), (2, 4), (3, 5), (8, 10), (1, 3)])

    def test_write_output(self):
        # write_output
        output_data = "6"
        write_output('test_output', output_data)
        with open('test_output', 'r') as test_output_file:
            result = test_output_file.read()
        self.assertEqual(result, "6")


if __name__ == '__main__':
    unittest.main()
