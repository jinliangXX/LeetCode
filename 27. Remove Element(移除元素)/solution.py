from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                is_true = False
                while right > left:
                    if nums[right] != val:
                        nums[left], nums[right] = nums[right], nums[left]
                        right -= 1
                        left += 1
                        is_true = True
                        break
                    right -= 1
                if not is_true:
                    return left
            else:
                left += 1
        return left


if __name__ == '__main__':
    so = Solution()
    re = so.removeElement([1], 1)
    print(re)
