# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.result = 0
        self.is_start = False

        def zhongxu(node: TreeNode):
            if not node:
                return
            zhongxu(node.left)
            if not self.is_start:
                if node.val == L:
                    self.result += node.val
                    self.is_start = True
            else:
                self.result += node.val
                if node.val == R:
                    self.is_start = False
                    return
            zhongxu(node.right)

        zhongxu(root)
        return self.result
