# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return list()
        self.result = list()

        def deep(node: TreeNode, target: int, now: List):
            now.append(node.val)
            if not node.left and not node.right:
                if target == node.val:
                    self.result.append(now)
            else:
                if node.left:
                    now_left = now.copy()
                    deep(node.left, target - node.val, now_left)
                if node.right:
                    now_right = now.copy()
                    deep(node.right, target - node.val, now_right)

        deep(root, sum, list())
        return self.result
