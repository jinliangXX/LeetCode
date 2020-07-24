class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[1 for _ in range(N + 1)] for _ in range(K)]
        dp[0] = [i for i in range(N + 1)]
        dp = [[0] + i[1:] for i in dp]
        for i in range(1, K):
            for j in range(2, N + 1):
                result = None
                for k in range(1, j + 1):
                    now = max(dp[i - 1][k - 1] + 1, 1 + dp[i][j - k])
                    result = min(result, now) if result else now
                dp[i][j] = result
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.superEggDrop(K=2, N=6))
