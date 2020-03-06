from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right = 1, 2
        result = list()
        now = 3
        while right <= (target + 1) // 2:
            if now == target:
                result.append([i for i in range(left, right + 1, 1)])
                now -= left
                left += 1
            elif now < target:
                right += 1
                now += right
            else:
                now -= left
                left += 1
        return result

if __name__ == '__main__':
    so = Solution()
    print(so.findContinuousSequence(15))
