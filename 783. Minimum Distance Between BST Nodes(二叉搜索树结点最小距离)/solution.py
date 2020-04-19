# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.result = 100
        self.front_num = -100

        def zhongxu(node: TreeNode):
            if not node:
                return
            zhongxu(node.left)
            self.result = min(self.result, abs(
                self.front_num - node.val)) if self.front_num is not None else self.result
            self.front_num = node.val
            zhongxu(node.right)

        zhongxu(root)
        return self.result
