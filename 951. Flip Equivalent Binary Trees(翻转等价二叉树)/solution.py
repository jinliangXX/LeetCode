# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            one = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right,
                                                                            root2.right)
            two = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right,
                                                                             root2.left)
            return one or two
        else:
            return False
