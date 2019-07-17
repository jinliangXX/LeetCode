import heapq
from collections import Counter

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_nums = Counter(nums)
        return heapq.nlargest(k, map_nums.keys(), key=map_nums.get)


if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    re = so.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(re)
'''
result = list()
        if not nums or k < 1:
            return result
        map_num = dict()
        for num in nums:
            map_num[num] = map_num.get(num, 0) + 1
        result = sorted(map_num.items(), key=lambda item: item[1], reverse=True)
        return [result[i][0] for i in range(k)]
'''
