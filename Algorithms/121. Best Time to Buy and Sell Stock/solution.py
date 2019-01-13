class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if len(prices) < 1:
            return 0
        min_num = prices[0]
        for i, price in enumerate(prices):
            if i < 1:
                continue
            min_num = min(min_num, prices[i - 1])
            result = max(result, price - min_num)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
