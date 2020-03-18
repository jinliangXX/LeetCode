# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def get_result(node: TreeNode):
            if not node:
                return
            get_result(node.right)
            self.sum += node.val
            node.val = self.sum
            get_result(node.left)

        get_result(root)
        return root
