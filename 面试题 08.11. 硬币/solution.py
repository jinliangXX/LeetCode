class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 1000000007
        dp = [1 for _ in range(n + 1)]
        coins = [5, 10, 25]
        for coin in coins:
            for i in range(coin, n + 1):
                dp[i] += dp[i - coin]
        return dp[-1] % mod
