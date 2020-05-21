from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_0, last_1 = 0.0, float("-inf")
        last_last_0 = 0.0
        for i, price in enumerate(prices):
            last_0, last_1, last_last_0 = max(last_1 + price, last_0), max(
                last_last_0 - price, last_1), last_0
        return int(last_0)
