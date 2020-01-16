import sys


class Solution:

    def get_num(self, n: int) -> int:
        result, money = [[1 for _ in range(n + 1)] for _ in range(7)], [0, 1, 5, 10, 20,
                                                                        50, 100]
        for i in range(2, 7):
            for j in range(2, n + 1):
                if j >= money[i]:
                    result[i][j] = result[i - 1][j] + result[i][j - money[i]]
                else:
                    result[i][j] = result[i - 1][j]
        return result[-1][-1]


if __name__ == '__main__':
    so = Solution()
    n = int(sys.stdin.readline().strip('\n'))
    print(so.get_num(n))
