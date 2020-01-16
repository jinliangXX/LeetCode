class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        result = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        result[0][0] = True
        for i in range(1, n + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i - 1]
            else:
                result[0][i] = False
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    result[i][j] = result[i - 1][j - 1]
                if p[j - 1] == '*':
                    result[i][j] = result[i][j - 1] or result[i - 1][j]
        return result[m][n]


if __name__ == '__main__':
    so = Solution()
    re = so.isMatch("aa", "*")
    print(re)
