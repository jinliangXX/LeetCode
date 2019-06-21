from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or not k:
            return
        length = len(nums)
        k %= length
        now = 0
        begin = now
        num = nums[now]
        for i in range(length - 1):
            now += k
            if now >= length:
                now -= length
            if now == begin:
                nums[begin] = num
                begin += 1
                now = begin
                num = nums[now]
                continue
            nums[now], num = num, nums[now]
        nums[begin] = num


if __name__ == '__main__':
    so = Solution()
    re = [1, 2, 3, 4, 5, 6]
    so.rotate(re, 2)

    print(re)
