from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while left < len(nums):
            if nums[left] != 0:
                left += 1
                continue
            right = max(left + 1, right)
            while right < len(nums):
                if nums[right] == 0:
                    right += 1
                    continue
                now = nums[left]
                nums[left] = nums[right]
                nums[right] = now
                break
            left += 1


'''
left = 0
        while left < len(nums):
            if nums[left] != 0:
                left += 1
                continue
            right = left + 1
            while right < len(nums):
                if nums[right] == 0:
                    right += 1
                    continue
                now = nums[left]
                nums[left] = nums[right]
                nums[right] = now
                break
            left += 1
'''
'''
        if 0 not in nums:
            return
        right = nums.index(0)
        while right < len(nums):
            if nums[right] == 0:
                right += 1
                continue
            index = nums.index(0)
            nums[index] = nums[right]
            nums[right] = 0
'''
if __name__ == '__main__':
    so = Solution()
    re = [0, 1, 0, 3, 12]
    so.moveZeroes(re)
    print(re)
