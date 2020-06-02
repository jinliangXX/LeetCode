from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last, last_last = 0, 0
        for cos in cost:
            last, last_last = min(last, last_last) + cos, last
        return min(last, last_last)
