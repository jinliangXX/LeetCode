class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False]
        for i in range(2, N + 1):
            now = False
            for j in range(1, i):
                if i % j == 0 and not dp[i - j - 1]:
                    now = True
            dp.append(now)
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    print(so.divisorGame(3))
