# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return list()
        result = list()

        def bottom(node: TreeNode, deep):
            if not node:
                return
            if deep == 0:
                result.append(node.val)
            bottom(node.left, deep - 1)
            bottom(node.right, deep - 1)

        def top(node: TreeNode):
            if not node:
                return -1
            left_result = top(node.left)
            left_result += 1 if left_result >= 0 else 0
            right_result = top(node.right)
            right_result += 1 if right_result >= 0 else 0
            if node == target:
                bottom(node, K)
            elif left_result == K or right_result == K:
                result.append(node.val)
            elif 0 < left_result < K:
                bottom(node.right, K - left_result - 1)
            elif 0 < right_result < K:
                bottom(node.left, K - right_result - 1)
            return max(left_result, right_result) if node != target else 0

        top(root)
        return result
