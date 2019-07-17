from collections import deque

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k < 1:
            return list()
        left, right = 0, k
        queue = deque()
        for i, num in enumerate(nums[left:right]):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
        result = list([nums[queue[0]]])
        while right < len(nums):
            if queue and queue[0] == left:
                queue.popleft()
            left += 1
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()
            queue.append(right)
            right += 1
            result.append(nums[queue[0]])
        return result


if __name__ == '__main__':
    so = Solution()
    so.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
