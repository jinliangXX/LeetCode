from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> \
            List[int]:
        result = list()
        if target in nums:
            left = 0
            right = len(nums) - 1
            while left <= right:
                m = int((left + right) / 2)
                midd = nums[m]
                if target <= midd:
                    right = m - 1
                else:
                    left = m + 1
            right = left
            while right < len(nums):
                if nums[right] != target:
                    break
                right += 1
            result.append(left)
            result.append(right - 1)
            return result
        else:
            return [-1, -1]


if __name__ == '__main__':
    so = Solution()
    re = so.searchRange([1, 2, 3], 2)
    print(re)

    test = [1, 2, 3, 4, 5]
    print(test[:, [1, 2, 3]])

'''
result.append(nums.index(target))
            result.append(
                len(nums) - nums[::-1].index(target) - 1)
'''
