from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        up, down = 1, 1
        for i, num in enumerate(nums):
            if i < 1:
                continue
            if num > nums[i - 1]:
                up = down + 1
            elif num < nums[i - 1]:
                down = up + 1
        return max(up, down)
