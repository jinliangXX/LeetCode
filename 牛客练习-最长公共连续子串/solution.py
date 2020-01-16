import sys


class Solution:

    def get_num(self, s1: str, s2: str) -> int:
        results, max_len = [[0 for _ in range(len(s2) + 1)] for _ in
                            range(len(s1) + 1)], 0
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    results[i][j] = results[i - 1][j - 1] + 1
                    if results[i][j] > max_len:
                        max_len = results[i][j]
        return max_len


if __name__ == '__main__':
    so = Solution()
    s1 = sys.stdin.readline().strip('\n')
    s2 = sys.stdin.readline().strip('\n')
    print(so.get_num(s1, s2))


'''
最长公共子序列：
DP：
if A[x-1] == B[y-1]   c[x][y] = c[x-1][y-1] + 1
if A[x-1] != B[y-1]   c[x][y] = max(c[x-1][y],c[x][y-1])
'''