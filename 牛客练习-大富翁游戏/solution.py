import sys


class Solution:

    def get_num(self, num: int) -> int:
        return 2 ** (num - 1)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip('\n'))
    so = Solution()
    print(so.get_num(n))
