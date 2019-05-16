class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        global_result = [[0, 0, 0]] * len(prices)
        local_result = [[0, 0, 0]] * len(prices)
        for i, price in enumerate(prices):
            if i < 1:
                continue
            diff = price - prices[i - 1]
            local_result[i][0] = 0
            local_result[i][1] = max(
                global_result[i - 1][0] + max(diff, 0),
                local_result[i - 1][1] + diff)
            local_result[i][2] = max(
                global_result[i - 1][1] + max(diff, 0),
                local_result[i - 1][2] + diff)
            global_result[i][0] = 0
            global_result[i][1] = max(
                global_result[i - 1][1], local_result[i][1])
            global_result[i][2] = max(
                global_result[i - 1][2], local_result[i][2])

        return max(global_result[len(prices) - 1][1],
                   global_result[len(prices) - 1][2])


if __name__ == '__main__':
    solution = Solution()
    input = [3, 3, 5, 0, 0, 3, 1, 4]
    print(solution.maxProfit([7, 6, 4, 3, 1]))
