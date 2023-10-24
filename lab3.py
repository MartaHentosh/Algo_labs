class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None

    queue = [tree]

    while queue:
        node = queue.pop(0)
        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return tree


def print_binary_tree(tree):
    if tree:
        print(tree.value)
        print_binary_tree(tree.left)
        print_binary_tree(tree.right)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

print("Default:")
print_binary_tree(root)

inverted_tree = invert_binary_tree(root)

print("\nChanged:")
print_binary_tree(inverted_tree)
