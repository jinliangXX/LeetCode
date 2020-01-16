class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while left < right:
            mid = (left + right + 1) // 2
            if mid ** 2 < x:
                left = mid
            elif mid ** 2 == x:
                left = mid
            else:
                right = mid - 1

        return left


# 二分法
# 牛顿法

if __name__ == '__main__':
    so = Solution()
    re = so.mySqrt(4)
    print(re)
