# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.result = True
        self.num = None

        def get_result(node: TreeNode):
            if not node:
                return None
            if self.num is None:
                self.num = node.val
            else:
                if self.num != node.val:
                    self.result = False
            get_result(node.left)
            get_result(node.right)

        get_result(root)
        return self.result
