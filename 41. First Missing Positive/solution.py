from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            if num < 1 or num > len(nums) or num == i + 1 or \
                    nums[num - 1] == num:
                i += 1
                continue
            now = nums[num - 1]
            nums[num - 1] = num
            nums[i] = now
        for j, num in enumerate(nums):
            if j != num - 1:
                return j + 1
        return len(nums) + 1


if __name__ == '__main__':
    so = Solution()
    so.firstMissingPositive([1, 1])
