# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_result(node: TreeNode, result):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
            else:
                get_result(node.left, result)
                get_result(node.right, result)

        result1, result2 = list(), list()
        get_result(root1, result1)
        get_result(root2, result2)

        return result1 == result2
