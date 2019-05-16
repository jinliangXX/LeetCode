from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        fast = nums[fast]
        fast = nums[fast]
        slow = nums[slow]
        while fast != slow:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
        slow_new = 0
        while slow != slow_new:
            slow = nums[slow]
            slow_new = nums[slow_new]
        return slow



