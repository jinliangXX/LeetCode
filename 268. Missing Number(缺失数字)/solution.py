from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result


'''
        if not nums:
            return 0
        nums.append(-1)
        for i in range(len(nums)):
            while nums[i] != -1 and nums[i] != i:
                now = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = now
        return nums.index(-1)
'''

if __name__ == '__main__':
    so = Solution()
    so.missingNumber(
        [9, 6, 4, 2, 3, 5, 7, 0, 1])
