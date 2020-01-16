import sys
from typing import List


class Solution:

    def get_num(self, n: int, a: List, b: List, c: List) -> int:
        index = 0 if a[0] > b[0] else n - 1
        if index == n - 1:
            cache, result = set(), a[-1]
            for i in range(n - 2, -1, -1):
                if i in cache:
                    continue
                if a[i - 1] > b[i - 1]:
                    result += a[i - 1]
                    cache.add(i - 1)
                result += b[i]
            return result
        if index == 0:
            result = a[0]
            for i in range(1, n):
                result += b[i]
            return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip('\n'))
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = list(map(int, sys.stdin.readline().strip().split()))
    c = list(map(int, sys.stdin.readline().strip().split()))
    so = Solution()
    print(so.get_num(n, a, b, c))
