# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        result = None
        list_p = self.get_list(root, p)
        list_q = self.get_list(root, q)
        for index in range(min(len(list_p), len(list_q))):
            if list_p[index] is list_q[index]:
                result = list_p[index]
        return result

    def get_list(self, root: 'TreeNode',
                 target: 'TreeNode'):
        if root is target:
            return [target]
        else:
            if root.left is not None:
                next_result = self.get_list(root.left,
                                            target)
                if next_result is not None:
                    result = [root]
                    result.extend(next_result)
                    return result
            if root.right is not None:
                next_result = self.get_list(root.right,
                                            target)
                if next_result is not None:
                    result = [root]
                    result.extend(next_result)
                    return result
        return None
