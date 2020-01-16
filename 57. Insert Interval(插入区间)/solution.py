from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[
        List[int]]:
        if not intervals:
            return [newInterval]
        result = list()
        is_insert, is_inserted = False, False
        for nums in intervals:
            if is_insert:
                if is_inserted:
                    result.append(nums)
                else:
                    if newInterval[1] >= nums[0]:
                        newInterval[1] = max(newInterval[1], nums[1])
                    else:
                        result.append(newInterval)
                        result.append(nums)
                        is_inserted = True
            else:
                if newInterval[0] <= nums[1]:
                    if newInterval[1] >= nums[0]:
                        newInterval[0], newInterval[1] = min(newInterval[0],
                                                             nums[0]), max(
                            newInterval[1], nums[1])
                        is_insert = True
                    else:
                        result.append(newInterval)
                        result.append(nums)
                        is_inserted = True
                        is_insert = True
                else:
                    result.append(nums)
        if not is_inserted:
            result.append(newInterval)
        return result


if __name__ == '__main__':
    so = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(so.insert(intervals, newInterval))
