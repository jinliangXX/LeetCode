from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        now = 0
        now_num = 0
        for num in nums:
            if now == 0:
                now_num = num
                now = 1
            else:
                if now_num == num:
                    now += 1
                else:
                    now -= 1
        return now_num


'''
        if len(nums) == 0:
            return 0
        result_dict = dict()
        now = len(nums) / 2
        for num in nums:
            result_dict[num] = result_dict.get(num, 0) + 1
            if result_dict[num] > now:
                return num
        return 0
'''
