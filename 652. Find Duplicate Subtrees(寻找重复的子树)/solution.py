# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = collections.Counter()
        result = list()

        def get_result(node: TreeNode):
            if not node:
                return '#'
            left_str = get_result(node.left)
            right_str = get_result(node.right)
            now_str = str(node.val) + left_str + right_str
            count[now_str] += 1
            if count[now_str] == 2:
                result.append(node)
            return now_str

        get_result(root)
        return result
