class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result_no = 0
        result_yes = 0
        for i, num in enumerate(nums):
            now = result_no
            result_no = max(result_yes, result_no)
            result_yes = now + num
        return max(result_yes, result_no)
