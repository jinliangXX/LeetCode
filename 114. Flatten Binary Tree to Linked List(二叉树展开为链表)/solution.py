# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.now = None

        def get_result(node: TreeNode):
            if not node:
                return
            get_result(node.right)
            get_result(node.left)
            node.right = self.now
            node.left = None
            self.now = node

        get_result(root)
