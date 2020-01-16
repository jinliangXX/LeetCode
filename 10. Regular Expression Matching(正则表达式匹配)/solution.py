class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        result[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                result[i][0] = result[i - 1][0]
            else:
                result[i][0] = False
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == '*':
                    if i - 2 >= 0 and p[i - 2] == '.':
                        result[i][j] = True
                    else:
                        result[i][j] = result[i - 1][j] or (
                                j - 1 < 0 or (s[j - 2] == s[j - 1]) and result[i - 1][
                            j - 1])
                elif p[i - 1] == '.' or p[i - 1] == s[j - 1]:
                    result[i][j] = result[i - 1][j - 1]
                else:
                    result[i][j] = False
        return result[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.isMatch('aab', 'c*a*b'))
