class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for size in range(1, n):
            for i in range(1, n + 1):
                j = i + size
                if j > n:
                    continue
                dp[i][j] = min(
                    num + max(dp[i][num - 1], dp[num + 1][j]) for num in range(i, j))
        return dp[1][n]


if __name__ == '__main__':
    so = Solution()
    print(so.getMoneyAmount(7))
