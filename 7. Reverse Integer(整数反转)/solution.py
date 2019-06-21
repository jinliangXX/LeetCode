class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        isFu = False
        if x < 0:
            isFu = True
        while x != 0:
            if isFu:
                now = (x % -10)
            else:
                now = x % 10
            print(now)
            if result > int((2 ** 31 - 1) / 10) or (
                    result == int((2 ** 31 - 1) / 10) // 10 and now > 7):
                return 0
            if result < int(-(2 ** 31) / 10) or (
                    result == int(-(2 ** 31) / 10) and now < -8):
                return 0

            result = result * 10 + now
            x = int(x / 10)
        return result


if __name__ == '__main__':
    print(-123 % -10)
    so = Solution()
    re = so.reverse(-123)
    print(re)
