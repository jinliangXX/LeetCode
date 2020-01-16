import sys
from typing import List


class Solution:


    '''
    最优解法为栈
    '''


def get_num(self, nums: List) -> int:
    result = 0
    for index, num in enumerate(nums):
        left, right = index, index + 1
        while left >= 0 and nums[left] >= num:
            left -= 1
        left += 1
        while right < len(nums) and nums[right] >= num:
            right += 1
        if (right - left) * num > result:
            result = (right - left) * num
    return result


if __name__ == '__main__':
    so = Solution()
    n = int(sys.stdin.readline().strip('\n'))
    nums = list(map(int, sys.stdin.readline().strip().split()))
    print(so.get_num(nums))
