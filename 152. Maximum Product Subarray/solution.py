from typing import List


class Solution(object):
    def maxProduct(self, nums: List):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        f = g = res = nums[0]
        for i in range(1, N):
            pre_f, pre_g = f, g
            f = max(pre_f * nums[i], nums[i], pre_g * nums[i])
            g = min(pre_f * nums[i], nums[i], pre_g * nums[i])
            res = max(res, f)
        return res
