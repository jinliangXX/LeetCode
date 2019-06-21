from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        for i in range(len(nums)):
            if nums[i] != nums[left]:
                left += 1
                nums[left] = nums[i]
        return left + 1


'''
        if not nums:
            return 0
        left, right = 0, 0
        while right < len(nums) and left < len(nums):
            if nums.index(nums[left]) != left:
                right = max(left + 1, right)
                while right < len(nums):
                    if nums.index(nums[right]) == right:
                        nums[left], nums[right] = nums[right], nums[left]
                        break
                    right += 1
                if right >= len(nums):
                    break
            left += 1
        return left
'''

if __name__ == '__main__':
    so = Solution()
    input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    re = so.removeDuplicates(input)
    print(re)
    print(input)
