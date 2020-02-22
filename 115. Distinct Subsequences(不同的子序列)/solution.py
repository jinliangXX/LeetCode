class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t:
            return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
        dp[0][0] = 1 if s[0] == t[0] else 0
        for i in range(len(t)):
            for j in range(max(i, 1), len(s)):
                if t[i] == s[j]:
                    if i == 0:
                        dp[i][j] = dp[i][j - 1] + 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.numDistinct("babgbag", "bag"))
