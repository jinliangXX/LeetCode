class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ago = list()
        while True:
            if n in ago:
                return False
            ago.append(n)
            n = str(n)
            total = 0
            for num in n:
                total += int(num) ** 2
            if total == 1:
                return True
            n = total


if __name__ == '__main__':
    so = Solution()
    so.isHappy(19)
