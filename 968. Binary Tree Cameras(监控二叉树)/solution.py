# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 0

        def get_result(node: TreeNode):
            if not node:
                return 0
            left_result = get_result(node.left) + 1
            right_result = get_result(node.right) + 1
            if max(left_result, right_result) == 2:
                self.result += 1
                return 2
            elif max(left_result, right_result) == 3:
                if min(left_result, right_result) == 2:
                    self.result += 1
                    return 2
                else:
                    return 0
            else:
                return 1

        num = get_result(root)
        return self.result if num != 1 else self.result + 1
