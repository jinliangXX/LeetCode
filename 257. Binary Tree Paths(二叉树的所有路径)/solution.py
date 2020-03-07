# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = list()
        if not root:
            return result

        def get_result(node: TreeNode, last: str):
            if not last:
                last = str(node.val)
            else:
                last += '->' + str(node.val)
            if not node.left and not node.right:
                result.append(last)
            if node.left:
                get_result(node.left, last)
            if node.right:
                get_result(node.right, last)

        get_result(root, None)
        return result
