import unittest
from lab3_lvl2 import BinaryTree , branchSums
class TestBranchSums(unittest.TestCase):
    def test_example_case(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        self.assertEqual(branchSums(root), 24)

    def test_only_root(self):
        root = BinaryTree(1)
        self.assertEqual(branchSums(root), 0)

    def test_left_leaf_only(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        self.assertEqual(branchSums(root), 2)

    def test_full_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        self.assertEqual(branchSums(root), 4 + 6)

if __name__ == "__main__":
    unittest.main()