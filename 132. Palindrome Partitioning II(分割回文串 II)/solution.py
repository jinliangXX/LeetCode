class Solution:
    def minCut(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                if j + i < len(s):
                    if i == 0:
                        dp[j][j + i] = True
                    else:
                        if s[j] == s[j + i] and (i == 1 or dp[j + 1][j + i - 1]):
                            dp[j][j + i] = True
        result = [i for i in range(len(s))]
        for i in range(len(s)):
            if dp[0][i]:
                result[i] = 0
                continue
            result[i] = min([result[j] + 1 for j in range(i) if dp[j + 1][i]])
        return result[-1]
