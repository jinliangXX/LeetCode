from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        last = 0
        for i in range(len(grid[0])):
            dp[0][i] = grid[0][i] + last
            last = dp[0][i]
        last = 0
        for j in range(len(grid)):
            dp[j][0] = grid[j][0] + last
            last = dp[j][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    input = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(so.minPathSum(input))
