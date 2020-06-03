import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        result = 0
        if not nums:
            return result
        nums_dict = collections.Counter(nums)
        dp, last_num = list(), None
        for i, num in enumerate(sorted(nums_dict.keys())):
            if i == 0:
                dp.append([num * nums_dict[num], 0])
                last_num = num
                continue
            if num == last_num + 1:
                dp.append([dp[-1][1] + num * nums_dict[num], max(dp[-1])])
            else:
                dp.append([max(dp[-1]) + num * nums_dict[num], max(dp[-1])])
            last_num = num
        return max(dp[-1])


if __name__ == '__main__':
    so = Solution()
    print(so.deleteAndEarn([2, 2, 3, 3, 3, 4]))
