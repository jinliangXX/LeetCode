class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if (mid + 1) ** 2 <= x:
                left = mid + 1
            else:
                right = mid

        return left


# 二分法
# 牛顿法

if __name__ == '__main__':
    so = Solution()
    re = so.mySqrt(8)
    print(re)
