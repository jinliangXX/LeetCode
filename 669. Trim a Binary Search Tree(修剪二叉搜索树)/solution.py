# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return
        if L < root.val < R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        elif L == root.val:
            root.left = None
            root.right = self.trimBST(root.right, L, R)
        elif R == root.val:
            root.right = None
            root.left = self.trimBST(root.left, L, R)
        elif root.val < L:
            root = self.trimBST(root.right, L, R)
        else:
            root = self.trimBST(root.left, L, R)
        return root
