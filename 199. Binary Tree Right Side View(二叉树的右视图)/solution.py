# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = list()
        if not root:
            return result

        def get_result(node: TreeNode, deep: int):
            if not node:
                return
            if deep >= len(result):
                result.append(node.val)
            get_result(node.right, deep + 1)
            get_result(node.left, deep + 1)

        get_result(root, 0)
        return result
