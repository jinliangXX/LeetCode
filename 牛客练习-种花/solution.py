import sys
from typing import List


class Solution:

    def get_num(self, nums: List, n: int) -> int:
        result, left, right = 0, 0, 0
        while left < n:
            if nums[left] != 0:
                right = left + 1
                while right < n:
                    if nums[right] == 0:
                        if right - left == 1:
                            break
                        else:
                            now = min(nums[left:right])
                            for num in nums[left:right]:
                                num -= now
                            result += now
                            right = left + 1
                            continue
                    if right == n - 1 and right - left > 0:
                        now = min(nums[left:])
                        for i in range(left, n):
                            nums[i] -= now
                        result += now
                        right = left + 1
                        continue
                    right += 1
            left += 1
        result += sum(nums)
        return result

        pass


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip('\n'))
    nums = list(map(int, sys.stdin.readline().strip().split()))
    so = Solution()
    print(so.get_num(nums, n))
