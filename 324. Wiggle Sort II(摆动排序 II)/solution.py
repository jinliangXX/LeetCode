import math
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return
        nums.sort(reverse=True)
        half = math.floor(len(nums) / 2)
        nums[::2], nums[1::2] = nums[half:], nums[0:half]
