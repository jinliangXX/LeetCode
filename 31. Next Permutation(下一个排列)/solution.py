from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reserve(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if not nums or len(nums) <= 1:
            return
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        break
                left, right = i, len(nums) - 1
                reserve(left, right)
                return
        left, right = 0, len(nums) - 1
        reserve(left, right)
