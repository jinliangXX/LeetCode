# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_deep(node: TreeNode):
            if not node:
                return 0
            return 1 + max(get_deep(node.left), get_deep(node.right))

        deep = get_deep(root)
        result = [['' for _ in range(2 ** deep - 1)] for _ in range(deep)]

        def fill(node: TreeNode, i=0, l=0, r=2 ** deep - 1 - 1):
            if not node:
                return
            j = (l + r) // 2
            result[i][j] = str(node.val)
            fill(node.left, i + 1, l, j - 1)
            fill(node.right, i + 1, j + 1, r)

        fill(root)
        return result
