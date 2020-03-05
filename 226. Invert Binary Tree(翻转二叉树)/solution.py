# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left_node, right_node = self.invertTree(root.left), self.invertTree(root.right)
        root.left, root.right = right_node, left_node
        return root
