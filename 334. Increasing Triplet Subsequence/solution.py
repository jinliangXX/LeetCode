import sys


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1:
            return False
        left = nums[0]
        right = sys.maxsize
        for num in nums:
            if num > right:
                return True
            elif left < num <= right:
                right = num
            else:
                left = num
        return False


