# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.result = None
        self.last = None
        if not root:
            return self.result

        def get_result(node: TreeNode):
            if not node:
                return
            get_result(node.left)
            if self.last is None:
                self.last = node.val
            else:
                now = abs(self.last - node.val)
                if self.result is None:
                    self.result = now
                else:
                    self.result = min(now, self.result)
                self.last = node.val
            get_result(node.right)

        get_result(root)
        return self.result
