from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 获取列表的第一个元素
        def takeFirst(elem):
            return elem[0]

        intervals.sort(key=takeFirst)
        result = list()
        for interval in intervals:
            if not result:
                result.append(interval)
                continue
            if interval[0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
            else:
                result.append(interval)
        return result
