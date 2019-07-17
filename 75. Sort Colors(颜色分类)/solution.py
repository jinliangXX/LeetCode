from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, now = 0, len(nums) - 1, 0
        while now <= right:
            if nums[now] == 0:
                nums[left], nums[now] = nums[now], nums[left]
                left += 1
                now += 1
            elif nums[now] == 1:
                now += 1
                continue
            else:
                nums[right], nums[now] = nums[now], nums[right]
                right -= 1
