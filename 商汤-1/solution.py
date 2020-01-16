import sys
from typing import List


class Solution:

    def get_index_b(self, n: int, m: int, nums_a: List, nums_b: List,
                    index_a: List) -> List:
        total, last, result = 0, 1, list()
        for i, index_a in enumerate(index_a[::-1]):
            if i == 0:
                total += index_a + 1
            else:
                total += index_a * last
            last *= nums_a[n - i - 1]
        last, total = 1, total - 1
        for i in range(1, m):
            last *= nums_b[i]
        for j in range(m - 1):
            now = int(total // last)
            result.append(now)
            total -= now * last
            last /= nums_b[j + 1]
        result.append(total)
        return result


if __name__ == '__main__':
    nums_a = list(map(int, sys.stdin.readline().strip().split()))
    n = nums_a.pop(0)
    nums_b = list(map(int, sys.stdin.readline().strip().split()))
    m = nums_b.pop(0)
    index_a = list(map(int, sys.stdin.readline().strip().split()))
    so = Solution()
    result = so.get_index_b(n, m, nums_a, nums_b, index_a)
    print(' '.join(str(i) for i in result))
