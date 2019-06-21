from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        if not nums:
            return result
        last = list()
        for num in nums:
            result = list()
            if not last:
                last.append([num])
                result.append([num])
                continue
            for la in last:
                for i, l in enumerate(la):
                    now = la.copy()
                    now.insert(i, num)
                    result.append(now)
                la.append(num)
                result.append(la)
            last = result
        return result


if __name__ == '__main__':
    so = Solution()
    re = so.permute([1, 2, 3])
    print(re)
