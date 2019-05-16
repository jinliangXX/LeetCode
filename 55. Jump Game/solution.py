class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= num:
                num = 1
            else:
                num += 1
        return True if num == 1 else False
