class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        result = 0
        for i in range(1, n):
            result = (m + result) % (i + 1)
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.lastRemaining(10, 17))
