# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = list()
        if not root:
            return result

        def get_result(node: TreeNode, deep=0):
            if not node:
                return
            if len(result) > deep:
                result[deep].append(node.val)
            else:
                result.append([node.val])
            get_result(node.left, deep + 1)
            get_result(node.right, deep + 1)

        get_result(root)
        result = [sum(re) / len(re) for re in result]
        return result
