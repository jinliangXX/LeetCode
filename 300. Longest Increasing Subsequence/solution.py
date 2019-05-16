from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        map_list = dict()
        result = 0
        for i, num in enumerate(nums[::-1]):
            index = len(nums) - i - 1
            now = 0
            for j, num_num in enumerate(nums[index + 1:]):
                if num_num > num:
                    now = max(now,
                              map_list[index + 1 + j] + 1)
            map_list[index] = now
            result = max(result, now)
        return result + 1


if __name__ == '__main__':
    so = Solution()
    so.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
