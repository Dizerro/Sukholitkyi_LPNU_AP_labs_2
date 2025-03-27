class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    def dfs(node, is_left):
        if not node:
            return 0
        if not node.left and not node.right and is_left:
            return node.value
        return dfs(node.left, True) + dfs(node.right, False)
    
    return dfs(root, False)

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)
root.left.right = BinaryTree(12)
root.left.left = BinaryTree(21)

print(branchSums(root))
