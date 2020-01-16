import sys
from typing import List


class Solution:

    def get_price(self, nums: List, n: int, x: int) -> int:
        result = [float('inf') for _ in range(x + 1)]
        for i in range(n):
            for j in range(x, -1, -1):
                if nums[i] >= j:
                    result[j] = min(result[j], nums[i])
                else:
                    result[j] = min(result[j], result[j - nums[i]] + nums[i])
        return result[-1]


if __name__ == '__main__':
    [n, k] = list(map(int, sys.stdin.readline().strip().split()))
    nums = list(map(int, sys.stdin.readline().strip().split()))
    so = Solution()
    print(so.get_price(nums, n, k))
