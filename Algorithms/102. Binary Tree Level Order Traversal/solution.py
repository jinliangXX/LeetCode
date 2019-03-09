# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.result = list()
        self.cal_num(root)
        return self.result

    def cal_num(self, root, weight=0):
        if root is None:
            return
        if len(self.result) <= weight:
            self.result.append(list())
        self.result[weight].append(root.val)
        num_left = weight
        self.cal_num(root.left, num_left + 1)
        self.cal_num(root.right, num_left + 1)
