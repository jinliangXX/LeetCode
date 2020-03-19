# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.result = 0

        def get_result(node: TreeNode):
            if not node: return 0
            left_result = get_result(node.left)
            right_result = get_result(node.right)
            self.result += abs(left_result - right_result)
            return node.val + left_result + right_result

        get_result(root)
        return self.result
