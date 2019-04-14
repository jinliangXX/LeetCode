from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = list()
        nums.reverse()
        for i, num in enumerate(nums):
            if i < 1:
                result.append(0)
                continue
            right = i
            left = 0
            while left <= right:
                m = int((left + right) / 2)
                if nums[m] >= num:
                    right = m - 1
                else:
                    left = m + 1
            nums.pop(i)
            nums.insert(right + 1, num)
            result.append(right + 1)
        result.reverse()
        return result


if __name__ == '__main__':
    so = Solution()
    re = so.countSmaller([5, 2, 6, 1])
    print(re)
