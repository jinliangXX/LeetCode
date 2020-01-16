class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        left, right = x, 0
        while left > right:
            right = right * 10 + left % 10
            left = left // 10
        return True if left == right or left == right // 10 else False


if __name__ == '__main__':
    so = Solution()
    so.isPalindrome(10)

'''
x = str(x)
        if not x:
            return True
        left, right = 0, len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True
'''
