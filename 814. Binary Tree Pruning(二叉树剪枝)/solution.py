# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left_result = self.pruneTree(root.left)
        right_result = self.pruneTree(root.right)
        if not left_result:
            root.left = None
        if not right_result:
            root.right = None
        if not left_result and not right_result and root.val == 0:
            return None
        else:
            return root
