import unittest

from lab3 import BinaryTree, invert_binary_tree, print_binary_tree


class TestBinaryTreeMethods(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        inverted_tree = invert_binary_tree(root)

        self.assertEqual(inverted_tree.value, 1)
        self.assertEqual(inverted_tree.left.value, 3)
        self.assertEqual(inverted_tree.right.value, 2)
        self.assertEqual(inverted_tree.left.left.value, 7)
        self.assertEqual(inverted_tree.left.right.value, 6)
        self.assertEqual(inverted_tree.right.left.value, 5)
        self.assertEqual(inverted_tree.right.right.value, 4)

    def test_print_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        import io
        from contextlib import redirect_stdout
        with io.StringIO() as buf, redirect_stdout(buf):
            print_binary_tree(root)
            output = buf.getvalue()

        expected_output = "1\n2\n4\n5\n3\n6\n7\n"
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
