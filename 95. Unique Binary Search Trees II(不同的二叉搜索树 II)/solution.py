# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            result = []
            if start > end:
                return [None]
            for i in range(start, end + 1):
                left_tree = generate(start, i - 1)
                right_tree = generate(i + 1, end)
                for l in left_tree:
                    for r in right_tree:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        result.append(node)
            return result

        return generate(1, n) if n else []
