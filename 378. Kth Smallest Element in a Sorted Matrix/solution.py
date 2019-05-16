import bisect

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]],
                    k: int) -> int:
        n = len(matrix[0])
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]
        while left < right:
            mid = (left + right) / 2
            count = 0
            for i in range(n):
                count += bisect.bisect_right(matrix[i], mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return int(left)
