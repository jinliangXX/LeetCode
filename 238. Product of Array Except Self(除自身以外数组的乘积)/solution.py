from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list()
        now = 1
        for num in nums:
            result.append(now)
            now *= num
        now = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= now
            now *= nums[i]
        return result
