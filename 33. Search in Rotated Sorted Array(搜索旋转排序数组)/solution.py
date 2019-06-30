from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if target <= nums[mid] or target > nums[right]:
                    right = mid
                else:
                    left = mid + 1
        return right if nums[right] == target else -1


if __name__ == '__main__':
    so = Solution()
    re = so.search([5, 1, 3], 1)
    print(re)
