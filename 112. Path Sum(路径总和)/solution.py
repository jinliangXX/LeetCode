# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        self.result = False

        def path(node: TreeNode, target):
            if not node.left and not node.right:
                if node.val == target:
                    self.result = True
            else:
                if node.left:
                    path(node.left, target - node.val)
                if node.right:
                    path(node.right, target - node.val)

        path(root, sum)

        return self.result
