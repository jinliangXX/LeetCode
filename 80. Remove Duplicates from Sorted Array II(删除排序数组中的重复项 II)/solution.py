from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #
        # def exchange(i, num, num_now):
        #     for i in range(i - num + 2, len(nums)):
        #         if i < len(nums) - num + 2:
        #             nums[i] = nums[i + num - 2]
        #         else:
        #             nums[i] = num_now
        #
        # num, last, i = 0, None, 0
        # while i < len(nums):
        #     if last is not None and nums[i] == last:
        #         num += 1
        #     elif last is not None and nums[i] < last:
        #         return i - num + 2 if num > 2 else i
        #     else:
        #         if last is not None and num > 2:
        #             exchange(i, num, last)
        #             i = i - num + 2
        #         num = 1
        #         last = nums[i]
        #     i += 1
        #
        # return len(nums) if num <= 2 else len(nums) - num + 2
        count, j = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == '__main__':
    so = Solution()
    input = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(so.removeDuplicates(input))
    pass
