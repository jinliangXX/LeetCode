from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        max_num = nums[0]
        max_num_last = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            max_num_last = max(max_num_last + num, num)
            max_num = max(max_num, max_num_last)
        return max_num
