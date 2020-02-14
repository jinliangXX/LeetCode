# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def cal_deep(node: TreeNode) -> int:
            if not node.left and not node.right:
                return 1
            elif node.left and node.right:
                return 1 + min(cal_deep(node.left), cal_deep(node.right))
            elif node.left:
                return 1 + cal_deep(node.left)
            else:
                return 1 + cal_deep(node.right)

        return cal_deep(root)
