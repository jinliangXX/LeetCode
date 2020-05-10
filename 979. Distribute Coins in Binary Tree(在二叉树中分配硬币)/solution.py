# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 0

        def get_result(node: TreeNode):
            if not node:
                return 1
            left = get_result(node.left)
            right = get_result(node.right)
            node.val -= 1 - left
            self.result += abs(1 - left)
            node.val -= 1 - right
            self.result += abs(1 - right)
            return node.val

        get_result(root)
        return self.result
