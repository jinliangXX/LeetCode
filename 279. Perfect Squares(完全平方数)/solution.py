import math


class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        for i in range(math.floor(math.sqrt(n)), 0, -1):
            for j in range(math.floor(math.sqrt(n - i ** 2)) + 1):
                if i ** 2 + j ** 2 == n:
                    if j > 0:
                        return 2
                    else:
                        return 1
        return 3


if __name__ == '__main__':
    so = Solution()
    so.numSquares(25)
