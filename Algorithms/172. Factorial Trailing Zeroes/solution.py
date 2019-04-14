class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 1:
            return 0
        result = 0
        i = 1
        while 5 ** i <= n:
            result += int(n / 5 ** i)
            i += 1
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.trailingZeroes(7))
