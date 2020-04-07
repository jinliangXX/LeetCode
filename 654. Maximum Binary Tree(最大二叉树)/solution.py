# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        max_num = max(nums)
        max_index = nums.index(max_num)
        node = TreeNode(max_num)
        node.left = self.constructMaximumBinaryTree(nums[:max_index])
        node.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return node


if __name__ == '__main__':
    so = Solution()
    input = [3, 2, 1, 6, 0, 5]
    print(so.constructMaximumBinaryTree(input))
