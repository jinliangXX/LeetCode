class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1 or k < 1:
            return 0
        if k >= len(prices):
            return self.get_run(prices)
        global_result = [[0 for i in range(k + 1)] for j in
                         range(len(prices))]
        local_result = [[0] * (k + 1)] * len(prices)
        for i, price in enumerate(prices):
            if i < 1:
                continue
            diff = price - prices[i - 1]
            for j in range(k + 1):
                if j < 1:
                    continue
                local_result[i][j] = max(
                    global_result[i - 1][j - 1] + max(diff,
                                                      0),
                    local_result[i - 1][j] + diff)
                global_result[i][j] = max(
                    global_result[i - 1][j],
                    local_result[i][j])
        return global_result[len(prices) - 1][k]

    def get_run(self, prices):
        result = 0
        for i, price in enumerate(prices):
            if i < 1:
                continue
            if price > prices[i - 1]:
                result += price - prices[i - 1]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
