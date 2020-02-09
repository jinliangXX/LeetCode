class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            now = 0
            for j in range(0, i):
                now += dp[i - j - 1] * dp[j]
            dp[i] = now
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    input = 3
    print(so.numTrees(input))
