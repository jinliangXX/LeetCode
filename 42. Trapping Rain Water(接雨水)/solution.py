from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result, last = 0, None
        if not height:
            return result
        left, right = 0, 0
        while left < len(height):
            while left < len(height) and height[left] == 0:
                left += 1
            if left >= len(height):
                return result
            right, now, max_h = left + 1, height[left], (left, 0, 0)
            while right < len(height) and height[right] < height[left]:
                now += height[right]
                if height[right] > max_h[1]:
                    max_h = (right, height[right], now)
                right += 1
            if right >= len(height):
                if max_h[0] == left:
                    break
                result += (max_h[0] - left) * max_h[1] - max_h[2] + height[left]
                left = max_h[0]
            else:
                result += (right - left) * height[left] - now
                left = right
        return result


if __name__ == '__main__':
    so = Solution()
    re = so.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(re)
