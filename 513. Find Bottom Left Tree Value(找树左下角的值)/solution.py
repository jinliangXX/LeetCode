# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.result = None
        self.deep = 0

        def get_result(node: TreeNode, deep=0):
            if node:
                deep += 1
                if deep > self.deep:
                    self.result = node.val
                    self.deep = deep
                get_result(node.left, deep)
                get_result(node.right, deep)

        get_result(root)
        return self.result
