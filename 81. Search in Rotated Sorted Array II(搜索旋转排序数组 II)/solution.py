from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[left]:
                if nums[mid] < target:
                    left = mid + 1
                elif target >= nums[left]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] == nums[left]:
                left += 1
            else:
                if nums[mid] > target:
                    right = mid
                elif target <= nums[right - 1]:
                    left = mid + 1
                else:
                    right = mid
        return False


if __name__ == '__main__':
    so = Solution()
    input = [1, 3, 1, 1]
    target = 3
    print(so.search(input, target))
