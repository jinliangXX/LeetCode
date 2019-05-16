from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                now = (right - left) * height[left]
                left = left + 1
            else:
                now = (right - left) * height[right]
                right = right - 1
            if now > max:
                max = now
        return max
