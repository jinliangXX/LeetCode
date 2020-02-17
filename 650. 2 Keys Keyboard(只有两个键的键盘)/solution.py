class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0
        result, now = 0, 2
        while n > 1:
            while n % now == 0:
                result += now
                n /= now
            now += 1
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.minSteps(6))
