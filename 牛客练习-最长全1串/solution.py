import sys
from typing import List


class Solution:

    def get_num(self, nums: List, k: int, n: int) -> int:
        left, right, length_k, result = 0, 0, 0, 0
        while right < n:
            if nums[right] == 0:
                if length_k == k:
                    result = max(result, right - left)
                    while nums[left] != 0:
                        left += 1
                    left += 1
                else:
                    length_k += 1
            right += 1
        result = max(result, right - left)
        return result


if __name__ == '__main__':
    [n, k] = list(map(int, sys.stdin.readline().strip().split()))
    nums = list(map(int, sys.stdin.readline().strip().split()))
    so = Solution()
    print(so.get_num(nums, k, n))
