class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        now = x
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= now
            now = now * now
            n = n // 2
        return result


'''
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        mid = n // 2
        return self.myPow(x, mid) * self.myPow(x, n - mid)
'''
if __name__ == '__main__':
    so = Solution()
    re = so.myPow(2.00000, 10)
    print(re)
