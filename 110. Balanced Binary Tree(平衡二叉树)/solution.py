# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.result = True

        def deep(node: TreeNode):
            if not node:
                return 0
            left_deep = deep(node.left)
            right_deep = deep(node.right)
            if abs(left_deep - right_deep) > 1:
                self.result = False
            return max(left_deep, right_deep) + 1

        deep(root)
        return self.result
