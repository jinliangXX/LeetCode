# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = list()

        def get_list(node: TreeNode):
            if not node:
                return
            get_list(node.left)
            nums.append(node.val)
            get_list(node.right)

        get_list(root)
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == k:
                return True
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return False
