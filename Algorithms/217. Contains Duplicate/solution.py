from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for num in nums:
            if a.get(num) is None:
                a[num] = 0
            else:
                return True
        return False
