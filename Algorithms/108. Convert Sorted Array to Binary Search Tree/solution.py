# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return None
        root = TreeNode(0)
        self.initBST(nums, root)
        return root

    def initBST(self, nums, root):
        if len(nums) < 2:
            root.val = nums[0]
        else:
            index = int(len(nums) / 2)
            root.val = nums[index]
            if index > 0:
                now = TreeNode(0)
                root.left = now
                self.initBST(nums[:index], now)
            if len(nums) - 1 > index:
                now = TreeNode(0)
                root.right = now
                self.initBST(nums[index + 1:], now)
