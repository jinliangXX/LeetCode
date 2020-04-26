# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.head = None
        self.now = None

        def get_result(node: TreeNode):
            if not node:
                return
            get_result(node.left)
            if not self.now:
                self.now = self.head = node
            else:
                self.now.left = None
                self.now.right = node
                self.now = node
            get_result(node.right)

        get_result(root)
        return self.head
