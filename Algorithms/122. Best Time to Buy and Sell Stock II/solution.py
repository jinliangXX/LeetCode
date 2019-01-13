class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        result = 0
        price_last = prices[0]
        for i, price in enumerate(prices):
            if price > price_last:
                result += price - price_last
            price_last = price
        return result
