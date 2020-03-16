# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        self.result = list()

        def dfs(node: TreeNode, deep=-1):
            if not node:
                return
            deep += 1
            if len(self.result) > deep:
                self.result[deep] = max(self.result[deep], node.val)
            else:
                self.result.append(node.val)
            dfs(node.left, deep)
            dfs(node.right, deep)

        dfs(root)
        return self.result
