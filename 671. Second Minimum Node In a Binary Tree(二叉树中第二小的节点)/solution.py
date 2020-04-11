# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        min_num = root.val
        self.result = -1

        def get_result(node: TreeNode):
            if not node:
                return
            if node.val == min_num:
                get_result(node.left)
                get_result(node.right)
            else:
                if self.result == -1 or node.val < self.result:
                    self.result = node.val

        get_result(root.left)
        get_result(root.right)
        return self.result
