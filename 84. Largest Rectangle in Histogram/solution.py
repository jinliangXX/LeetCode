from typing import List


class Solution:
    def largestRectangleArea(self,
                             heights: List[int]) -> int:
        max = 0
        for i, num in enumerate(heights):
            if i == len(heights) - 1 or heights[i + 1] < num:
                min = num
                left = i
                while left >= 0:
                    if heights[left] < min:
                        min = heights[left]
                    if (i - left + 1) * min > max:
                        max = (i - left + 1) * min
                    left -= 1
        return max


'''
max = 0
        for i, num in enumerate(heights):
            left = i
            right = i
            while left - 1 >= 0 and heights[left - 1] >= num:
                left -= 1
            while right + 1 < len(heights) and heights[
                right + 1] >= num:
                right += 1
            if (right - left + 1) * num > max:
                max = (right - left + 1) * num
        return max
'''
'''
max = 0
        left = 0
        right = 0
        for i, num in enumerate(heights):
            if i == 0 or heights[i - 1] < num:
                left = i
            elif heights[i - 1] == num:
                continue
            else:
                while left - 1 >= 0 and heights[
                    left - 1] >= num:
                    left -= 1
            right = i
            while right + 1 < len(heights) and heights[
                right + 1] >= num:
                right += 1
            if (right - left + 1) * num > max:
                max = (right - left + 1) * num
        return max
'''
